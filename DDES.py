import hashlib  # For generating fingerprints
import datetime  # For timestamps and logs
import json  # For storing offender logs and reports
import os  # For file operations


# ---------------------------
# 1. TRACE ORIGIN OF CONTENT
# ---------------------------
def trace_origin(source_url):
    """
    Trace the origin of harmful or defamatory content.
    Args:
        source_url (str): The URL of the defamatory content.
    Returns:
        dict: Metadata about the content's origin.
    """
    print("[INFO] Tracing origin of content...")

    # Simulate tracing metadata (this would be more complex in reality)
    origin_metadata = {
        "source_url": source_url,
        "traced_ip": "192.168.1.100",  # Placeholder IP address
        "server_location": "London, UK",
        "timestamp": datetime.datetime.now().isoformat(),
        "content_id": hashlib.sha256(source_url.encode()).hexdigest()
    }
    return origin_metadata


# ---------------------------
# 2. GENERATE CONTENT FINGERPRINT
# ---------------------------
def fingerprint_content(content_metadata):
    """
    Generate a unique digital fingerprint for content.
    Args:
        content_metadata (dict): Metadata returned by trace_origin.
    Returns:
        str: Unique fingerprint hash.
    """
    print("[INFO] Generating digital fingerprint...")

    # Combine source URL and timestamp to create a unique identifier
    fingerprint_base = f"{content_metadata['source_url']}{content_metadata['timestamp']}"
    fingerprint = hashlib.sha256(fingerprint_base.encode()).hexdigest()
    return fingerprint


# ---------------------------
# 3. CALCULATE FINANCIAL DAMAGES
# ---------------------------
def calculate_damage(financial_losses):
    """
    Estimate financial damage caused by defamation.
    Args:
        financial_losses (list): A list of estimated financial damages (£).
    Returns:
        float: Total estimated damages.
    """
    print("[INFO] Calculating financial damages...")

    if not financial_losses:
        return 0.0

    total_damage = sum(financial_losses)
    penalty = total_damage * 0.15  # Example penalty multiplier for punitive damages
    return round(total_damage + penalty, 2)


# ---------------------------
# 4. LOG OFFENDER INFORMATION
# ---------------------------
def log_offender(username, fingerprint, violation_type="Defamation"):
    """
    Log offender information into a structured file.
    Args:
        username (str): Offender's username.
        fingerprint (str): Content fingerprint.
        violation_type (str): Type of violation.
    Returns:
        bool: True if successfully logged.
    """
    print("[INFO] Logging offender information...")

    offender_data = {
        "username": username,
        "fingerprint": fingerprint,
        "violation_type": violation_type,
        "log_timestamp": datetime.datetime.now().isoformat()
    }

    log_file = "offender_logs.json"

    if not os.path.exists(log_file):
        with open(log_file, 'w') as file:
            json.dump([], file)  # Create an empty list if file doesn't exist

    with open(log_file, 'r+') as file:
        logs = json.load(file)
        logs.append(offender_data)
        file.seek(0)
        json.dump(logs, file, indent=4)

    return True


# ---------------------------
# 5. GENERATE FINAL REPORT
# ---------------------------
def generate_report(origin_data, fingerprint, damages, offender_username):
    """
    Generate a structured court-ready report.
    Args:
        origin_data (dict): Metadata from trace_origin.
        fingerprint (str): Content fingerprint.
        damages (float): Total damage estimate.
        offender_username (str): Offender's username.
    Returns:
        str: File path of the report.
    """
    print("[INFO] Generating court-ready report...")

    report_data = {
        "generated_on": datetime.datetime.now().isoformat(),
        "origin_data": origin_data,
        "fingerprint": fingerprint,
        "estimated_damages": f"£{damages}",
        "offender": offender_username
    }

    report_path = "court_ready_report.json"
    with open(report_path, 'w') as file:
        json.dump(report_data, file, indent=4)

    return report_path


# ---------------------------
# MAIN WORKFLOW
# ---------------------------
def main():
    try:
        # Step 1: Trace origin of defamatory content
        source = "https://example.com/defamatory-post"
        origin_data = trace_origin(source)
        print("\n[RESULT] Origin traced:", origin_data)

        # Step 2: Generate fingerprint for content
        fingerprint = fingerprint_content(origin_data)
        print("\n[RESULT] Fingerprint generated:", fingerprint)

        # Step 3: Calculate financial damages
        financial_data = [1500, 3200, 2100]  # Example financial impacts
        estimated_damages = calculate_damage(financial_data)
        print(f"\n[RESULT] Estimated Financial Damages: £{estimated_damages}")

        # Step 4: Log offender's information
        username = "offender_user"
        if log_offender(username, fingerprint):
            print(f"\n[RESULT] Offender '{username}' logged successfully.")

        # Step 5: Generate final report
        report_path = generate_report(origin_data, fingerprint, estimated_damages, username)
        print(f"\n[RESULT] Court-ready report generated at: {report_path}")

    except Exception as e:
        print(f"\n[ERROR]: {e}")


# ---------------------------
# SCRIPT ENTRY POINT
# ---------------------------
if __name__ == "__main__":
    main()
