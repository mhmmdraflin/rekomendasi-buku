% Fakta buku
buku('Clean Code', teknologi).
buku('The Pragmatic Programmer', teknologi).
buku('Harry Potter', fiksi).
buku('Sapiens', sejarah).
buku('Laskar Pelangi', fiksi).

% Aturan rekomendasi
rekomendasi(Judul, Minat) :- buku(Judul, Minat).