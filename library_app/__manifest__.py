{
  "name": "Syd Library Management",
  "summary": "Syd Manage Library Catalog and Book Lending",
  "author": "Michael Daoud",
  "website": "https://sydneytools.com.au",
  "version": "16.0.1",
  "depends": ["base"],
  "category": "Services/Library",
  "data": [
    "security/library_security.xml",
    "security/ir.model.access.csv",
    "views/book_view.xml",
    "views/library_menu.xml",
    "views/book_list_template.xml",
    ],
  "demo": [
    "data/res.partner.csv",
    "data/library.book.csv",
    "data/book_demo.xml",
    ],
  "application": True,
}
