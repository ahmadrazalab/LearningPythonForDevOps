
# 🧪 PYTHON FOR DEVOPS — 100 PRACTICE QUESTIONS

**Level: Beginner → Intermediate**

---

## 🟢 SECTION 1: Absolute Basics (1–15)

1. Write a Python script that prints **“Python is used in DevOps automation”**.

   * Explain how Python executes a script line by line.

2. Write a script that reads a value from an **environment variable** called `ENV` and prints it.

   * Explain what environment variables are and why DevOps uses them.

3. Write a script that takes a **command-line argument** (service name) and prints:

   ```
   Checking status of <service>
   ```

   * Explain how CLI arguments are used in CI/CD.

4. Write a script that checks whether Python is running inside a **virtual environment**.

   * Explain why virtual environments matter in DevOps.

5. Write a script that exits with:

   * Exit code `0` if successful
   * Exit code `1` if failed
   * Explain exit codes and how CI tools use them.

---

## 🟢 SECTION 2: Variables & Data Types (16–25)

6. Store EC2 instance details (id, type, state) using appropriate Python data types.

   * Explain why `dict` is preferred here.

7. Convert a JSON string (mock AWS response) into a Python object and print instance IDs.

8. Write a script that stores multiple server names in a list and loops through them.

9. Create a dictionary of services and their ports, then print each service and port.

10. Write a script that safely accesses a key that may not exist in a dictionary.

    * Explain why defensive coding is critical in automation.

---

## 🟢 SECTION 3: Control Flow (26–35)

11. Write a script that checks disk usage percentage and prints:

    * WARNING if >70%
    * CRITICAL if >90%

12. Write a script that loops through EC2 instance states and prints only **running** instances.

13. Write a script that retries an operation **3 times** before failing.

14. Write a script that skips unhealthy servers in a list.

15. Write a script that stops execution if a required config value is missing.

---

## 🟢 SECTION 4: Functions & Reusability (36–45)

16. Write a function that checks if a file exists and returns True/False.

17. Write a function that validates a service status and logs the result.

18. Write a reusable function that executes shell commands safely.

19. Write a function that formats log output consistently.

20. Explain why DevOps scripts should always use functions instead of copy-paste logic.

---

## 🟢 SECTION 5: File Handling (46–55)

21. Write a script that reads a log file and prints the number of ERROR lines.

22. Write a script that writes server health results to a file.

23. Read a JSON file containing AWS resource details and extract tags.

24. Read a YAML Kubernetes config and validate required fields.

25. Append new log entries without overwriting existing logs.

---

## 🟡 SECTION 6: OS & Linux Interaction (56–65)

26. Run the `df -h` command using Python and capture output.

27. Execute a shell command and handle non-zero exit codes.

28. Write a script that checks if a Linux service is running.

29. Capture both STDOUT and STDERR from a command.

30. Explain why `subprocess` is safer than `os.system`.

---

## 🟡 SECTION 7: Logging & Error Handling (66–75)

31. Configure Python logging with INFO and ERROR levels.

32. Write a script that logs failures instead of printing them.

33. Handle a file-not-found exception gracefully.

34. Add timestamps to log entries.

35. Explain why logging is mandatory in production automation.

---

## 🟡 SECTION 8: APIs & Networking (76–85)

36. Write a script that makes a GET request to an API and checks status code.

37. Handle API timeouts and retries.

38. Parse JSON response from an API and extract required values.

39. Send a POST request to a webhook (Slack-style).

40. Explain why APIs are central to DevOps automation.

---

## 🟡 SECTION 9: AWS Automation (86–95)

41. Write a script that lists EC2 instances using boto3.

42. Filter EC2 instances by tag.

43. Detect untagged AWS resources.

44. Check if EBS snapshots exist for today.

45. Generate a CSV report of EC2 instances.

46. Handle AWS authentication failures gracefully.

47. Explain IAM role usage in automation scripts.

48. Write a script that checks CloudWatch alarm status.

49. Validate that an S3 bucket exists before uploading files.

50. Explain why boto3 scripts must be region-aware.

---

## 🟡 SECTION 10: Kubernetes & CI/CD (96–100)

51. List all Kubernetes namespaces using Python.

52. Detect pods in CrashLoopBackOff.

53. Restart a Kubernetes deployment via Python.

54. Write a Python script that Jenkins can execute in a pipeline.

55. Exit pipeline execution on script failure.

56. Pass secrets securely to Python scripts in CI.

57. Explain why Python scripts should be idempotent.

58. Write a script that validates YAML before deployment.

59. Write a script that generates deployment reports.

60. Explain how Python fits into GitOps workflows.


