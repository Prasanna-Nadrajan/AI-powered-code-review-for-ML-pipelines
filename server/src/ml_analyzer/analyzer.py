import ast
import re
from rules import get_comprehensive_rules

class MLCodeReviewer:
    """
    Analyzes Python ML code based on a set of predefined rules.
    """

    def __init__(self):
        """Initializes the reviewer by loading the analysis rules."""
        self.rules = get_comprehensive_rules()

    def analyze_code(self, code):
        """
        Performs a comprehensive analysis of the given code snippet.
        It now checks for syntax errors first and stops if any are found.
        """
        # --- LOGIC FIX: Prioritize Syntax Check ---
        # First, try to parse the code. If it fails, it's a syntax error.
        syntax_issues = self._ast_analysis(code)
        if syntax_issues:
            # If there's a syntax error, the code is invalid.
            # Immediately return only this critical issue.
            return syntax_issues
        # -----------------------------------------

        # If the code is syntactically valid, proceed with other checks.
        issues = []
        lines = code.splitlines()

        # Generic pattern-based checks
        for category, details in self.rules.items():
            severity = details.get('severity', 'suggestion')
            if 'patterns' in details:
                for pattern, message in details.get('patterns', []):
                    if re.search(pattern, code, re.IGNORECASE):
                        line_num = self._find_line_for_pattern(lines, pattern)
                        issues.append({
                            'line': line_num,
                            'issue': message,
                            'severity': severity,
                            'category': category
                        })

        # Specific, more complex checks
        if 'feature_scaling' in self.rules:
            issues.extend(self._detect_scaling_issues(code, lines))

        return self._deduplicate_issues(issues)

    def _find_line_for_pattern(self, lines, pattern):
        """Finds the first line number matching a regex pattern."""
        for i, line in enumerate(lines, 1):
            if re.search(pattern, line, re.IGNORECASE):
                return i
        return 1

    def _detect_scaling_issues(self, code, lines):
        """Detects missing feature scaling for scale-sensitive algorithms."""
        issues = []
        rule_info = self.rules['feature_scaling']
        scale_sensitive = rule_info.get('scale_sensitive_algorithms', {})
        scalers = rule_info.get('scalers', [])

        for algorithm, full_name in scale_sensitive.items():
            if re.search(r'\b' + algorithm + r'\b', code) and not any(scaler in code for scaler in scalers):
                line_num = self._find_line_for_pattern(lines, r'\b' + algorithm + r'\b')
                issues.append({
                    'line': line_num,
                    'issue': f'{full_name} is sensitive to feature scaling. Consider using a scaler.',
                    'severity': 'warning',
                    'category': 'scaling'
                })
        return issues

    def _ast_analysis(self, code):
        """
        Performs AST-based analysis to find syntax errors.
        Returns a list containing the syntax error if found, otherwise an empty list.
        """
        try:
            ast.parse(code)
            return []  # No syntax error found
        except SyntaxError as e:
            # Return a list containing only the syntax error information
            return [{
                'line': e.lineno or 1,
                'issue': f'Fatal Syntax Error: {e.msg}',
                'severity': 'error', # 'error' will be treated as 'critical' by main.py
                'category': 'syntax'
            }]

    def _deduplicate_issues(self, issues):
        """Removes duplicate issues."""
        seen = set()
        unique_issues = []
        for issue in issues:
            identifier = (issue['issue'], issue.get('line', 1))
            if identifier not in seen:
                seen.add(identifier)
                unique_issues.append(issue)
        return unique_issues