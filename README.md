# queens-cb2

Monorepo for projects that support Queens Community Board 2. This root README is a landing page: it explains setup and lists projects. Each project has its own README with details and run instructions.

## Quick start

- Requirements: Python 3.10+ (see `requirements.txt`)
- Install dependencies once:

  ```bash
  pip install -r requirements.txt
  ```

- Go to a project folder and follow its README.

## Projects

| Project | Path | Description | Docs |
| --- | --- | --- | --- |
| Homepage • Link Grabber | `homepage/link_grabber/` | Scrapes homepage links, verifies status, and supports CSV upload. | [README](homepage/link_grabber/README.md) |

Add new projects as rows in this table and include a per-project README.

## Repository layout

```
.
├── LICENSE
├── README.md             # You are here
├── requirements.txt
└── homepage/
    └── link_grabber/
        ├── 01. all_link_grabber.ipynb
        ├── 02. link_verify.ipynb
        ├── 03_csv_uploader.py
        ├── 03_csv_uploader.ipynb (optional)
        ├── README_UPLOADER.md
        ├── START_HERE.md
        ├── COMPLETION_REPORT.md
        ├── links_table.csv
        ├── links_table_with_status.csv
        └── flow_chart/
            ├── 01.1 flow-chart.md
            └── 02.1 flow-chart.md
```

---

## 🤝 Contributing

We welcome contributions from Queens CB2 members, constituents, and community volunteers! Whether you're a developer, web designer, or just someone who cares about the community board's web presence, you can help.

### Ways to Contribute

1. **Found a Bug?**
   - Report it by opening an Issue
   - Or submit a Pull Request with a fix

2. **Have an Improvement?**
   - Add new features to make the tool better
   - Suggest improvements to the documentation
   - Optimize performance or add error handling

3. **Want to Help Verify Links?**
   - Run the tool and check the results
   - Verify that broken links are actually broken
   - Help update the Queens CB2 website URLs to fix links

### How to Submit a Pull Request

1. **Fork the repository**
   ```bash
   Click "Fork" button on GitHub
   ```

2. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Edit the files you want to improve
   - Test your changes thoroughly
   - Add comments to explain your code

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "Brief description of what you changed"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Open a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch and describe your changes
   - Click "Create Pull Request"

7. **Wait for Review**
   - A maintainer will review your changes
   - Make any requested updates
   - Once approved, your code will be merged!

### Pull Request Guidelines

Please follow these guidelines when submitting a PR:

✅ **Do**:
- Write clear commit messages
- Test your changes before submitting
- Update documentation if needed
- Reference any related issues

❌ **Don't**:
- Submit large changes without creating an Issue first
- Change unrelated code in your PR
- Add unnecessary dependencies

---

## 🐛 Reporting Issues

Found a problem? Help us fix it!

1. **Check if the issue already exists**
   - Search through existing Issues first

2. **Create a new Issue**
   - Click "Issues" tab
   - Click "New Issue"
   - Describe the problem clearly:
     - What are you trying to do?
     - What happened instead?
     - What did you expect to happen?
     - What step broke?

3. **Include helpful details**
   - Python version: `python --version`
   - Error messages (copy the full text)
   - Screenshot if relevant
   - Steps to reproduce the issue

---

## ❓ FAQ

**Q: Who is this project for?**  
A: Anyone in the Queens CB2 district who wants to suggest improvements, and current or future Board Members who want to use, adapt, or extend the tools for their workflows. All skill levels welcome.

**Q: How can I share suggestions or ideas without coding?**  
A: Open an Issue with the “suggestion” label and include:
- The page(s) or link(s) you’re referring to
- The problem or idea and why it helps CB2
- Any screenshots or files that help explain it

You can also help by testing results and giving feedback on proposed changes.

**Q: Do I need to be a programmer to contribute?**  
A: No. You can participate by filing suggestions, verifying links, running notebooks step-by-step, or improving docs. Code changes are optional and guided by each project’s README.


---

## 📞 Support & Community

- **Questions?** Open an Issue on GitHub
- **Want to contribute?** See the Contributing section above
- **Found a bug?** Please report it with as much detail as possible
- **Have ideas?** We'd love to hear them! Create an Issue to discuss

---

## 👥 Contributors

A big thank you to all CB2 members and community volunteers who have contributed to this project!

Want to see your name here? Contribute to the project!


---

**Last Updated**: November 2, 2025

🙏 Thank you for supporting Queens Community Board 2!


## License

This project is licensed under the MIT License — see `LICENSE`.


