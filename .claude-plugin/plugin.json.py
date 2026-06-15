{
  "schemaVersion": "1",
  "id": "pyxll-agent-skills",
  "name": "PyXLL Agent Skills",
  "version": "0.1.4",
  "description": "Agent skills for PyXLL that ensure AI always consults the live documentation — not outdated training data — when writing, configuring, or debugging PyXLL code.",
  "author": "PyXLL <support@pyxll.com>",
  "homepage": "https://www.pyxll.com",
  "skills": [
    {
      "id": "fetch-pyxll-docs",
      "name": "Fetch PyXLL Docs",
      "description": "Automatically fetches the authoritative PyXLL documentation before any PyXLL task, ensuring accurate use of the PyXLL API and configuration.",
      "path": "skills/fetch-pyxll-docs/SKILL.md"
    },
    {
      "id": "pywin32-excel-docs",
      "name": "PyWin32 Excel Docs",
      "description": "Reference for the Microsoft Excel COM API via pywin32.",
      "path": "skills/pywin32-excel-docs/SKILL.md"
    },
    {
      "id": "office-customui-xsd",
      "name": "Office CustomUI XSD",
      "description": "Reference for the Microsoft CustomUI XML scmema as used PyXLL for ribbon customization.",
      "path": "skills/office-customui-xsd/SKILL.md"
    }
  ]
}