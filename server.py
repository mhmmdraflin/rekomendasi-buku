from flask import Flask, request, redirect
import mysql.connector

app = Flask(__name__)

# Koneksi ke MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_rekomendasi"
)

@app.route('/')
def home():
    form_minat = """
    <h1 class="mb-4">Pilih Minat Anda</h1>
    <form action="/rekomendasi" method="post" class="mb-5">
        <label class="form-check"><input type="checkbox" name="minat" value="teknologi" class="form-check-input"> Teknologi</label><br>
        <label class="form-check"><input type="checkbox" name="minat" value="fiksi" class="form-check-input"> Fiksi</label><br>
        <label class="form-check"><input type="checkbox" name="minat" value="sejarah" class="form-check-input"> Sejarah</label><br><br>
        <button type="submit" class="btn btn-success">Cari Rekomendasi</button>
    </form>
    <a href="/buku" class="btn btn-primary mb-4">Kelola Data Buku (CRUD)</a>
    """
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
      <title>Rekomendasi Buku</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light p-4">
      <div class="container">
        {form_minat}
      </div>
    </body>
    </html>
    """

@app.route('/rekomendasi', methods=['POST'])
def rekomendasi():
    minat = request.form.getlist('minat')
    hasil = []
    cursor = db.cursor()

    try:
        for m in minat:
            query = "SELECT judul, image_url, author, tahun_terbit FROM buku WHERE minat = %s"
            cursor.execute(query, (m,))
            books = cursor.fetchall()

            if books:
                cards = ""
                for judul, image_url, author, tahun in books:
                    cards += f"""
                    <div class="card mb-3" style="max-width: 540px;">
                      <div class="row g-0">
                        <div class="col-md-4">
                          <img src="{image_url}" class="img-fluid rounded-start" alt="{judul}">
                        </div>
                        <div class="col-md-8">
                          <div class="card-body">
                            <h5 class="card-title">{judul}</h5>
                            <p class="card-text">Author: {author}</p>
                            <p class="card-text"><small class="text-muted">Tahun Terbit: {tahun}</small></p>
                          </div>
                        </div>
                      </div>
                    </div>
                    """
                hasil.append(cards)
            else:
                hasil.append(f"<div class='alert alert-warning'>Tidak ada rekomendasi untuk <b>{m}</b>.</div>")

    except mysql.connector.Error as err:
        hasil.append(f"<div class='alert alert-danger'>Database Error: {err}</div>")

    finally:
        cursor.close()

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
      <title>Hasil Rekomendasi</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light p-4">
      <div class="container">
        <h2 class="text-center mb-4">Hasil Rekomendasi</h2>
        {''.join(hasil)}
        <div class="text-center mt-4">
          <a href="/" class="btn btn-outline-secondary">← Kembali</a>
        </div>
      </div>
    </body>
    </html>
    """

@app.route('/buku')
def buku():
    cursor = db.cursor()
    cursor.execute("SELECT id, judul, minat, image_url, author, tahun_terbit FROM buku")
    books = cursor.fetchall()
    cursor.close()

    rows = ""
    for id, judul, minat, img, author, tahun in books:
        rows += f"""
        <tr>
            <td>{judul}</td>
            <td>{minat}</td>
            <td><img src="{img}" width="80"></td>
            <td>{author}</td>
            <td>{tahun}</td>
            <td>
                <a href="/edit/{id}" class="btn btn-warning btn-sm">Edit</a>
                <a href="/delete/{id}" class="btn btn-danger btn-sm" onclick="return confirm('Hapus?')">Hapus</a>
            </td>
        </tr>
        """

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Data Buku</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light p-4">
        <div class="container">
            <h1>Data Buku</h1>
            <a href="/tambah" class="btn btn-success mb-3">Tambah Buku</a>
            <table class="table table-bordered table-striped">
                <thead><tr><th>Judul</th><th>Minat</th><th>Gambar</th><th>Author</th><th>Tahun</th><th>Aksi</th></tr></thead>
                <tbody>{rows}</tbody>
            </table>
            <a href="/" class="btn btn-secondary">← Kembali ke Pilih Minat</a>
        </div>
    </body>
    </html>
    """

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        judul = request.form['judul']
        minat = request.form['minat']
        image_url = request.form['image_url']
        author = request.form['author']
        tahun = request.form['tahun']

        cursor = db.cursor()
        cursor.execute("INSERT INTO buku (judul, minat, image_url, author, tahun_terbit) VALUES (%s, %s, %s, %s, %s)",
                       (judul, minat, image_url, author, tahun))
        db.commit()
        cursor.close()
        return redirect('/buku')

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Tambah Buku</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light p-4">
        <div class="container">
            <h1>Tambah Buku</h1>
            <form method="post">
                <div class="mb-3"><input type="text" name="judul" class="form-control" placeholder="Judul" required></div>
                <div class="mb-3"><input type="text" name="minat" class="form-control" placeholder="Minat" required></div>
                <div class="mb-3"><input type="url" name="image_url" class="form-control" placeholder="Image URL" required></div>
                <div class="mb-3"><input type="text" name="author" class="form-control" placeholder="Author" required></div>
                <div class="mb-3"><input type="number" name="tahun" class="form-control" placeholder="Tahun Terbit" required></div>
                <button type="submit" class="btn btn-primary">Simpan</button>
                <a href="/buku" class="btn btn-secondary">Kembali</a>
            </form>
        </div>
    </body>
    </html>
    """

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cursor = db.cursor()
    if request.method == 'POST':
        judul = request.form['judul']
        minat = request.form['minat']
        image_url = request.form['image_url']
        author = request.form['author']
        tahun = request.form['tahun']

        cursor.execute("UPDATE buku SET judul=%s, minat=%s, image_url=%s, author=%s, tahun_terbit=%s WHERE id=%s",
                       (judul, minat, image_url, author, tahun, id))
        db.commit()
        cursor.close()
        return redirect('/buku')

    cursor.execute("SELECT judul, minat, image_url, author, tahun_terbit FROM buku WHERE id=%s", (id,))
    buku = cursor.fetchone()
    cursor.close()

    if buku:
        judul, minat, img, author, tahun = buku
        return f"""
        <!DOCTYPE html>
        <html>
        <head><title>Edit Buku</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"></head>
        <body class="bg-light p-4">
            <div class="container">
                <h1>Edit Buku</h1>
                <form method="post">
                    <div class="mb-3"><input type="text" name="judul" value="{judul}" class="form-control" required></div>
                    <div class="mb-3"><input type="text" name="minat" value="{minat}" class="form-control" required></div>
                    <div class="mb-3"><input type="url" name="image_url" value="{img}" class="form-control" required></div>
                    <div class="mb-3"><input type="text" name="author" value="{author}" class="form-control" required></div>
                    <div class="mb-3"><input type="number" name="tahun" value="{tahun}" class="form-control" required></div>
                    <button type="submit" class="btn btn-primary">Update</button>
                    <a href="/buku" class="btn btn-secondary">Kembali</a>
                </form>
            </div>
        </body>
        </html>
        """
    else:
        return "Buku tidak ditemukan."

@app.route('/delete/<int:id>')
def delete(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM buku WHERE id=%s", (id,))
    db.commit()
    cursor.close()
    return redirect('/buku')

if __name__ == '__main__':
    app.run(debug=True)
