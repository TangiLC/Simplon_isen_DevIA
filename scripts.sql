
--SELECT * FROM ventes;

--3.a CA TOTAL
--SELECT SUM(c3*c4) AS CA_TOTAL FROM ventes;

--3.b ventes par produit
--SELECT c2,  SUM(c4) AS total_ventes,  SUM(c3 * c4) AS ca_produit FROM ventes GROUP BY c2;

--3.c ventes par région
--SELECT c5,  SUM(c4) AS total_ventes,  SUM(c3 * c4) AS ca_produit FROM ventes GROUP BY c5;