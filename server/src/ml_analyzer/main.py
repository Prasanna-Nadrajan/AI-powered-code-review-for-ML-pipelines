# import sys
# import json
# import os
# import uuid

# # CORRECTED: This now correctly imports from the 'analyzer.py' file
# # that is in the same directory.
# from analyzer import MLCodeReviewer

# def main(file_path):
#     """
#     Analyzes the code in the given file and prints a single JSON object
#     formatted for the React frontend.
#     """
#     try:
#         with open(file_path, 'r', encoding='utf-8') as f:
#             code = f.read()
#     except Exception as e:
#         print(json.dumps({"error": f"Failed to read file: {str(e)}"}))
#         return

#     # 1. Run your existing code analyzer
#     reviewer = MLCodeReviewer()
#     issues_from_analyzer = reviewer.analyze_code(code)

#     # 2. Translate your analyzer's output into the format the frontend needs
#     critical_issues_count = 0
#     warning_count = 0
#     performance_count = 0 

#     all_issues_for_frontend = []
#     for issue in issues_from_analyzer:
#         severity = issue.get('severity', 'suggestion')
        
#         if severity == 'critical' or severity == 'error':
#             frontend_severity = 'critical'
#             critical_issues_count += 1
#         elif severity == 'warning':
#             frontend_severity = 'warning'
#             warning_count += 1
#         else:
#             frontend_severity = 'info'

#         if severity == 'positive':
#             continue

#         all_issues_for_frontend.append({
#             "id": str(uuid.uuid4()),
#             "severity": frontend_severity,
#             "title": issue.get('category', 'Code Issue').replace('_', ' ').title(),
#             "description": issue.get('issue', 'No description available.'),
#             "lineStart": issue.get('line', 1),
#             "lineEnd": issue.get('line', 1),
#             "suggestions": f"Review this {issue.get('category', 'issue')} for potential improvements."
#         })

#     # 3. Create the final JSON object that the frontend components will display
#     final_json_output = {
#         "id": str(uuid.uuid4()),
#         "projectName": os.path.basename(file_path),
#         "status": "completed",
#         "overallScore": max(0, 100 - (critical_issues_count * 10) - (warning_count * 2)),
#         "criticalIssues": critical_issues_count,
#         "warnings": warning_count,
#         "performanceIssues": performance_count,
#         "coverage": 95,
#         "createdAt": "2025-07-26T12:00:00Z",
#         "issues": all_issues_for_frontend
#     }

#     # 4. Print the final result as a single JSON string.
#     print(json.dumps(final_json_output, indent=4))

# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         file_to_analyze = sys.argv[1]
#         main(file_to_analyze)
#     else:
#         print(json.dumps({"error": "No file path was provided to the analysis script."}))

import sys
import json
import os
import uuid
from analyzer import MLCodeReviewer

def main(file_path):
    """
    Analyzes the code in the given file and prints a single JSON object
    formatted for the React frontend.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
    except Exception as e:
        print(json.dumps({"error": f"Failed to read file: {str(e)}"}))
        return

    # --- LOGIC FIX: Handle Empty or Whitespace-Only Files ---
    if not code.strip():
        # If the file is empty, create a specific report and exit.
        empty_file_report = {
            "id": str(uuid.uuid4()),
            "projectName": os.path.basename(file_path),
            "status": "completed",
            "overallScore": 0,
            "criticalIssues": 1, # Treat this as one critical issue
            "warnings": 0,
            "performanceIssues": 0,
            "coverage": 0,
            "createdAt": "2025-07-26T12:00:00Z", # Placeholder
            "issues": [{
                "id": str(uuid.uuid4()),
                "severity": "critical",
                "title": "Empty File Uploaded",
                "description": "The uploaded file contains no code to analyze. Please upload a valid Python script.",
                "lineStart": 1,
                "lineEnd": 1,
                "suggestions": "Ensure the file is saved correctly and contains Python code."
            }]
        }
        print(json.dumps(empty_file_report, indent=4))
        return
    # ----------------------------------------------------

    # 1. Run your existing code analyzer
    reviewer = MLCodeReviewer()
    issues_from_analyzer = reviewer.analyze_code(code)

    # 2. Translate your analyzer's output into the format the frontend needs
    critical_issues_count = 0
    warning_count = 0
    performance_count = 0 

    all_issues_for_frontend = []
    for issue in issues_from_analyzer:
        severity = issue.get('severity', 'suggestion')
        
        if severity == 'critical' or severity == 'error':
            frontend_severity = 'critical'
            critical_issues_count += 1
        elif severity == 'warning':
            frontend_severity = 'warning'
            warning_count += 1
        else:
            frontend_severity = 'info'

        if severity == 'positive':
            continue

        all_issues_for_frontend.append({
            "id": str(uuid.uuid4()),
            "severity": frontend_severity,
            "title": issue.get('category', 'Code Issue').replace('_', ' ').title(),
            "description": issue.get('issue', 'No description available.'),
            "lineStart": issue.get('line', 1),
            "lineEnd": issue.get('line', 1),
            "suggestions": f"Review this {issue.get('category', 'issue')} for potential improvements."
        })

    # 3. Create the final JSON object that the frontend components will display
    final_json_output = {
        "id": str(uuid.uuid4()),
        "projectName": os.path.basename(file_path),
        "status": "completed",
        "overallScore": max(0, 100 - (critical_issues_count * 10) - (warning_count * 2)),
        "criticalIssues": critical_issues_count,
        "warnings": warning_count,
        "performanceIssues": performance_count,
        "coverage": 95,
        "createdAt": "2025-07-26T12:00:00Z",
        "issues": all_issues_for_frontend
    }

    # 4. Print the final result as a single JSON string.
    print(json.dumps(final_json_output, indent=4))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_to_analyze = sys.argv[1]
        main(file_to_analyze)
    else:
        print(json.dumps({"error": "No file path was provided to the analysis script."}))
