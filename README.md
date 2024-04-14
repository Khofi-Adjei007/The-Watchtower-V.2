# Policing System Documentation

## Overview
The Policing System project aims to streamline the process of case reporting and record-keeping within law enforcement agencies. By implementing a cloud-based docketing system, the project intends to simplify the recording, storage, and accessibility of case information nationwide. Equipped with peripherals such as cameras, fingerprint scanners, and microphones, each station will have the necessary tools to collect comprehensive evidence for investigations.

## Objectives
- Enable officers to create comprehensive dockets containing text, images, and audiovisual elements, with automatic PDF generation upon submission.
- Implement real-time call reception and location tracking functionalities for emergency calls.
- Distribute newly created reports across all nodes of the system, ensuring accessibility by authorized personnel.

## Features

### Authentication and Access Control
- Officers' credentials are authenticated against staff IDs and biometric data (Face ID or fingerprint) for secure login/logout.
- Access to system functionalities is restricted based on user roles and permissions.

### Docket Creation
- Officers can initiate new dockets, inputting details such as case information, evidence images, scanned fingerprints, and timestamps.
- The system automatically populates default data fields like date, time, reporting station, and reporting officer.

### Record Search
- Authorized officers can search the system for records of suspects and past case histories.
- Search results display relevant information, including suspect details, category (criminal, civil, etc.), and case status.

### Officer and Suspect Information Management
- Officers' information includes personal details, contact information, rank, station assignment, staff ID, qualifications, and department.
- Suspects' information encompasses full name, place of birth, Ghana Card number, address, employment status, criminal history, and last known interactions with law enforcement.

### PDF Docket Generation
- Dockets are saved as print-ready PDF files protected by passwords, accessible only to station officers and reporting officers/CID.
- PDF headers contain officer's name, date/time, station code, district/city, and agency logo/emblem for identification and authenticity.
- Text content within the PDF appears typed with a typewriter font to signify confidentiality and authority.

### Preview and Verification
- A preview feature allows officers to review docket details before submission, ensuring accuracy and completeness.

## Basic Functionalities
- Search functionality enables quick retrieval of case records.
- Authentication mechanisms ensure secure access to system features.
- PDF generation facilitates standardized and secure documentation.
- Real-time display of current time, date, and station ID provides contextual information.

## Usage
1. **Login/Logout**: Authenticate with staff ID and biometric data (Face ID or fingerprint).
2. **Docket Creation**: Initiate new dockets, input case details, attach evidence, and verify before submission.
3. **Record Search**: Search for suspect records and review case histories.
4. **Officer Information Management**: Maintain accurate records of officer details, qualifications, and assignments.
5. **Suspect Information Management**: Record comprehensive details of suspects, including personal, criminal, and interaction history.
6. **PDF Docket Generation**: Generate secured PDF dockets with header information and typewriter-style text content.

## Contributors
- [Khofi Adjei Future Kingsford]
- [Future Industries]

## License
This project is licensed under the [License Name]. See the LICENSE.md file for details.

For detailed implementation instructions and user guidelines, please refer to the project documentation provided within the codebase.