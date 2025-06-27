# My Cloud Resume CRC

Welcome to **My Cloud Resume CRC**! This project is a cloud-based resume website, designed to showcase your professional experience, skills, and projects using modern web technologies and cloud principles.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

This repository contains the source code for a personal resume website, designed as a cloud project following the [Cloud Resume Challenge (CRC)](https://cloudresumechallenge.dev/). The site presents your resume in an interactive and visually appealing format, leveraging cloud technologies for deployment and scalability.

## Features

- Responsive and modern design
- Showcases professional experience, education, and skills
- Live project links and contact information
- Cloud-friendly structure for easy deployment (e.g., AWS S3, Azure Blob Storage)
- Optionally includes a visitor counter (using serverless backend)

## Tech Stack

- **HTML**: Structure and layout (66%)
- **CSS**: Styling and responsive design (26.2%)
- **JavaScript**: Interactive features (2.4%)
- **Python**: Backend/serverless functionality (5.4%)  
  (e.g., API for visitor counter or contact form)

## Getting Started

#### Prerequisites

- [Git](https://git-scm.com/)
- Basic knowledge of HTML/CSS/JS
- (Optional) Cloud CLI tools (e.g., AWS CLI, Azure CLI)

#### Clone the Repository

```bash
git clone https://github.com/gus-hub-tech/my-cloud-resume-crc.git
cd my-cloud-resume-crc
```

#### Running Locally

Simply open `index.html` in your browser to preview the resume site locally.

#### Modifying Content

- Update the HTML files with your own resume information.
- Customize styles in the CSS files.
- Add or modify interactivity in the JavaScript files.

## Project Structure

```
my-cloud-resume-crc/
├── index.html
├── css/
│   └── styles.css
├── js/
│   └── main.js
├── backend/
│   └── (Python scripts or Lambda functions)
├── assets/
│   └── images, icons, etc.
└── README.md
```

- `index.html`: Main entry point of the website
- `css/`: All styling files
- `js/`: JavaScript for interactive features
- `backend/`: Python code for serverless functions (e.g., visitor counter)
- `assets/`: Images and other assets

## Deployment

You can deploy this site to popular cloud platforms. Here are some options:

### Deploy to AWS S3 (Static Website Hosting)

1. Build/prepare your site
2. Upload files to your S3 bucket
3. Enable static website hosting
4. (Optional) Set up a custom domain with Route 53

### Serverless Backend (Optional)

If using a visitor counter or contact form:

- Deploy Python Lambda functions (see `/backend`)
- Use API Gateway to expose endpoints
- Connect frontend JavaScript to the API

## Contributing

Contributions are welcome! Please open a pull request or issue to suggest improvements.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Inspired by the Cloud Resume Challenge.**  
Happy deploying!
