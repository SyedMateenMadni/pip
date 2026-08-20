from flask import Flask, jsonify
from datetime import datetime, timezone
import time

app = Flask(__name__)
START_TIME = time.time()

books = [
    {"id": 1, "title": "The Pragmatic Programmer", "author": "David Thomas", "genre": "Technology", "year": 1999, "available": True},
    {"id": 2, "title": "Clean Code",               "author": "Robert C. Martin", "genre": "Technology", "year": 2008, "available": True},
    {"id": 3, "title": "Atomic Habits",             "author": "James Clear",      "genre": "Self-Help",  "year": 2018, "available": False},
    {"id": 4, "title": "Sapiens",                   "author": "Yuval Noah Harari","genre": "History",    "year": 2011, "available": True},
    {"id": 5, "title": "The Phoenix Project",       "author": "Gene Kim",         "genre": "Technology", "year": 2013, "available": False},
]

@app.get("/")
def index():
    rows = "".join(
        f"<tr><td>{b['id']}</td><td>{b['title']}</td><td>{b['author']}</td>"
        f"<td>{b['genre']}</td><td>{b['year']}</td>"
        f"<td style='color:{'green' if b['available'] else 'red'}'>{'Available' if b['available'] else 'Checked Out'}</td></tr>"
        for b in books
    )
    available = sum(1 for b in books if b["available"])
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <title>Book Inventory</title>
  <style>
    body {{ font-family: Arial, sans-serif; padding: 32px; background: #f4f6f9; color: #222; }}
    h1   {{ color: #2c3e50; }}
    .stats {{ display: flex; gap: 16px; margin: 16px 0; }}
    .badge {{ background: #2c3e50; color: #fff; padding: 8px 16px; border-radius: 6px; font-size: 14px; }}
    table {{ border-collapse: collapse; width: 100%; background: #fff; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
    th, td {{ padding: 12px 16px; border-bottom: 1px solid #e0e0e0; text-align: left; }}
    th {{ background: #2c3e50; color: #fff; }}
    tr:last-child td {{ border-bottom: none; }}
  </style>
</head>
<body>
  <h1>📚 Book Inventory</h1>
  <div class="stats">
    <span class="badge">Total: {len(books)}</span>
    <span class="badge">Available: {available}</span>
    <span class="badge">Checked Out: {len(books) - available}</span>
  </div>
  <table>
    <thead><tr><th>#</th><th>Title</th><th>Author</th><th>Genre</th><th>Year</th><th>Status</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
</body>
</html>"""

@app.get("/health")
def health():
    return jsonify({
        "status": "healthy",
        "uptime_seconds": round(time.time() - START_TIME),
        "total_books": len(books),
        "available_books": sum(1 for b in books if b["available"]),
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

@app.get("/api/books")
def get_books():
    return jsonify({"count": len(books), "books": books})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
