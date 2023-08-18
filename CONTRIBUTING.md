## 🚀 Contributing to XRPL-Swap Project

Welcome to the XRPL-Swap development guide! Here are the rules and guidelines to ensure smooth collaboration and consistency throughout the project.

### 1. Starting Point

Before diving into changes, please either discuss them with the team or post them in the issues or discussion section following the provided templates. Whether it's a new feature or a potential bug fix, getting feedback or documenting it ensures we avoid duplicate efforts and potential conflicts.

### 2. Fork & Create a Branch

- **Fork the repo** and then clone it locally:

  - HTTPS:

    ```bash
    git clone https://github.com/<your-username>/xrpl-swap.git
    ```

  - SSH:

    ```bash
    git clone git@github.com:/<your-username>/xrpl-swap.git
    ```

- **Navigate to your local fork**: `cd xrpl-swap`.

- **Create a branch** for your feature or bugfix:

  ```bash
  git checkout -b <branch-name>
  ```

### 3. Setup Your Environment

Before you begin your work, ensure your environment is correctly configured:

- **Poetry Setup**:

  If you haven't installed Poetry yet, you can do so by following the instructions [here](https://python-poetry.org/docs/).

  ```bash
  poetry install
  ```

  This will install all the project's dependencies and add your project to the virtual environment.

- **Pre-commit Setup**:

  We use `pre-commit` to enforce a coding style and catch common issues. Install it with:

  ```bash
  pip install pre-commit
  ```

  Then, set it up for the repo with:

  ```bash
  pre-commit install
  ```

### 4. Committing Your Changes

Before committing, ensure you've set up `pre-commit` hooks as mentioned earlier in the setup section. This ensures that your code adheres to the project's coding standards.

Follow the commit message convention using gitmoji:

```
<emoji><type>: <description>
```

Where `<emoji>` and `<type>` can be one of the following:

- ✨`feat`: For introducing new features
- 🐛`fix`: For bug fixes
- 🎨`style`: For changes related to styling and appearance
- 📝`docs`: Documentation-only changes
- ♻️`refactor`: Code refactoring without changing any logic
- ⚡️`perf`: Code changes to improve performance
- ✅`test`: Adding missing tests or corrections
- 🔧`chore`: Build process or auxiliary tool changes
- 🔀`merge`: Merging branches or introducing changes from upstream
- ⏪`revert`: Reverting changes

Example:

```
✨feat: Add new API endpoint for prices
```

Make sure your commit messages clearly describe what the commit does. In addition to the above, you can use other gitmojis that fit the nature of the change. Consult the [gitmoji guide](https://gitmoji.dev) for more emojis and their meanings.

### 5. Submitting a Pull Request

- Push your branch to your fork on GitHub:

  ```bash
  git push origin <branch-name>
  ```

- From your fork, **open a pull request** in the main repo.

- Once the pull request is approved and merged, you can pull the changes from the main repo and delete your branch (if you wish).

---

## 📖 Further Reading

- [Poetry Documentation](https://python-poetry.org/docs/)
- [Pre-commit Documentation](https://pre-commit.com/)
- [Git and GitHub Learning Resources](https://docs.github.com/en/get-started/quickstart/git-and-github-learning-resources)

---

Your collaboration is what makes this project thrive! Let's keep up the great work together. 🚀

---
