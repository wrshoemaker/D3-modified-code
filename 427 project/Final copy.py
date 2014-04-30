import csv, itertools, json

def cluster(rows):
    result = []
    data = sorted(rows, key=lambda r: r[1])
    for k, g in itertools.groupby(rows, lambda r: r[0]):
        group_rows = [row[1:] for row in g]

        if len(row[1:]) == 1:
               result.append({"name": row[0], "size": row[1].strip(),"size": int(row[1])})
        else:
               result.append({"name": k,"children": cluster(group_rows)})

    return result

if __name__ == '__main__':
    s = '''\
life,k__Archaea, p__Crenarchaeota, c__Thaumarchaeota, o__Nitrososphaerales, f__Nitrososphaeraceae, g__Candidatus Nitrososphaera,101071,1000
life,k__Archaea, p__Euryarchaeota, c__[Parvarchaea], o__YLA114, f__, g__,denovo2449,1000
life,k__Archaea,,,,,,denovo668,1000
life,k__Bacteria, p__Acidobacteria, c__, o__, f__, g__,denovo2218,1000
life,k__Bacteria, p__Acidobacteria, c__Acidobacteria-5, o__, f__, g__,3490229,1000
life,k__Bacteria, p__Acidobacteria, c__Acidobacteria-6, o__iii1-15, f__, g__,509442,1000
life,k__Bacteria, p__Acidobacteria, c__Acidobacteria-6, o__iii1-15, f__, g__,704612,1000
life,k__Bacteria, p__Acidobacteria, c__Chloracidobacteria, o__, f__, g__,55946,1000
life,k__Bacteria, p__Acidobacteria, c__Chloracidobacteria, o__, f__, g__,636687,2000
life,k__Bacteria, p__Acidobacteria, c__Holophagae, o__Holophagales, f__Holophagaceae, g__,144899,1000
life,k__Bacteria, p__Acidobacteria, c__Holophagae, o__Holophagales, f__Holophagaceae,,3252661,1000
life,k__Bacteria, p__Acidobacteria, c__MVS-40, o__, f__, g__,583865,1000
life,k__Bacteria, p__Acidobacteria, c__MVS-40, o__, f__, g__,669483,1000
life,k__Bacteria, p__Acidobacteria, c__Solibacteres, o__Solibacterales, f__Solibacteraceae, g__Candidatus Solibacter,304016,1000
life,k__Bacteria, p__Acidobacteria, c__Solibacteres, o__Solibacterales, f__Solibacteraceae, g__Candidatus Solibacter,789791,2000
life,k__Bacteria, p__Actinobacteria, c__Acidimicrobiia, o__Acidimicrobiales, f__, g__,255515,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Actinosynnemataceae, g__,12978,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Cellulomonadaceae, g__Cellulomonas,235695,6000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Cellulomonadaceae,,101394,10000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Corynebacteriaceae, g__Corynebacterium,1093318,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Frankiaceae, g__,73544,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Frankiaceae, g__,240553,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Frankiaceae, g__,252713,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Frankiaceae, g__,254635,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Frankiaceae, g__,887457,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Frankiaceae, g__,denovo804,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Intrasporangiaceae, g__,248784,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Intrasporangiaceae, g__,581352,2000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Intrasporangiaceae,,denovo2879,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Kineosporiaceae, g__Kineosporia,12697,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Microbacteriaceae,,535579,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Microbacteriaceae,,739867,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Microbacteriaceae,,1874551,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Micromonosporaceae, g__,214718,2000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Micromonosporaceae,,109779,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Nakamurellaceae, g__,147604,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Nocardioidaceae, g__,208818,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Nocardioidaceae, g__,237339,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Nocardioidaceae, g__,778968,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Nocardioidaceae, g__,1124464,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Nocardioidaceae, g__Aeromicrobium,1798209,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Nocardioidaceae,,414150,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Nocardioidaceae,,1024759,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Sporichthyaceae, g__,243367,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Williamsiaceae, g__Williamsia,534222,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales, f__Williamsiaceae, g__Williamsia,526776,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales,,,557925,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales,,,1113503,1000
life,k__Bacteria, p__Actinobacteria, c__Actinobacteria, o__Actinomycetales,,,denovo2458,9000
life,k__Bacteria, p__Actinobacteria, c__Thermoleophilia, o__Gaiellales, f__Gaiellaceae, g__,240172,1000
life,k__Bacteria, p__Actinobacteria, c__Thermoleophilia, o__Gaiellales, f__Gaiellaceae, g__,572125,1000
life,k__Bacteria, p__Actinobacteria, c__Thermoleophilia, o__Gaiellales, f__Gaiellaceae, g__,1143223,1000
life,k__Bacteria, p__Actinobacteria, c__Thermoleophilia, o__Solirubrobacterales, f__Patulibacteraceae, g__,denovo4,1000
life,k__Bacteria, p__Actinobacteria, c__Thermoleophilia, o__Solirubrobacterales, f__Solirubrobacteraceae, g__,252308,2000
life,k__Bacteria, p__Actinobacteria, c__Thermoleophilia, o__Solirubrobacterales,,,533434,1000
life,k__Bacteria, p__Actinobacteria, c__Thermoleophilia, o__Solirubrobacterales,,,567702,1000
life,k__Bacteria, p__Bacteroidetes, c__Bacteroidia, o__Bacteroidales, f__, g__,538931,1000
life,k__Bacteria, p__Bacteroidetes, c__Bacteroidia, o__Bacteroidales, f__, g__,540669,1000
life,k__Bacteria, p__Bacteroidetes, c__Bacteroidia, o__Bacteroidales, f__, g__,1115108,1000
life,k__Bacteria, p__Bacteroidetes, c__Bacteroidia, o__Bacteroidales, f__, g__,denovo1029,1000
life,k__Bacteria, p__Bacteroidetes, c__Bacteroidia, o__Bacteroidales, f__, g__,denovo1364,1000
life,k__Bacteria, p__Bacteroidetes, c__Bacteroidia, o__Bacteroidales, f__, g__,denovo1368,1000
life,k__Bacteria, p__Bacteroidetes, c__Bacteroidia, o__Bacteroidales, f__, g__,denovo240,1000
life,k__Bacteria, p__Bacteroidetes, c__Bacteroidia, o__Bacteroidales, f__, g__,denovo2741,1000
life,k__Bacteria, p__Bacteroidetes, c__Bacteroidia, o__Bacteroidales, f__, g__,denovo3011,1000
life,k__Bacteria, p__Bacteroidetes, c__Bacteroidia, o__Bacteroidales, f__, g__,denovo362,1000
life,k__Bacteria, p__Bacteroidetes, c__Bacteroidia, o__Bacteroidales, f__, g__,denovo57,1000
life,k__Bacteria, p__Bacteroidetes, c__Bacteroidia, o__Bacteroidales, f__, g__,denovo881,2000
life,k__Bacteria, p__Bacteroidetes, c__Bacteroidia, o__Bacteroidales, f__Bacteroidaceae, g__,156012,1000
life,k__Bacteria, p__Bacteroidetes, c__Bacteroidia, o__Bacteroidales, f__Rikenellaceae, g__,denovo2405,1000
life,k__Bacteria, p__Bacteroidetes, c__Bacteroidia, o__Bacteroidales,,,denovo1763,1000
life,k__Bacteria, p__Bacteroidetes, c__Bacteroidia, o__Bacteroidales,,,denovo2687,1000
life,k__Bacteria, p__Bacteroidetes, c__Flavobacteriia, o__, f__, g__,144803,1000
life,k__Bacteria, p__Bacteroidetes, c__Flavobacteriia, o__Flavobacteriales, f__Cryomorphaceae, g__,103229,1000
life,k__Bacteria, p__Bacteroidetes, c__Flavobacteriia, o__Flavobacteriales, f__Cryomorphaceae, g__,640461,1000
life,k__Bacteria, p__Bacteroidetes, c__Flavobacteriia, o__Flavobacteriales, f__Flavobacteriaceae, g__Elizabethkingia,577339,3000
life,k__Bacteria, p__Bacteroidetes, c__Flavobacteriia, o__Flavobacteriales, f__Flavobacteriaceae,,849907,1000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales, f__, g__,242136,1000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales, f__, g__,denovo1465,1000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales, f__Chitinophagaceae, g__,160651,1000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales, f__Chitinophagaceae, g__,216350,1000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales, f__Chitinophagaceae, g__,771274,1000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales, f__Chitinophagaceae, g__,953500,1000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales, f__Chitinophagaceae, g__,1039568,1000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales, f__Chitinophagaceae, g__,denovo2740,1000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales, f__Chitinophagaceae, g__Chitinophaga,58620,3000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales, f__Chitinophagaceae, g__Chitinophaga,164755,1000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales, f__Chitinophagaceae,,358280,1000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales, f__Chitinophagaceae,,570934,2000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales, f__Flammeovirgaceae, g__A4,220782,1000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales, f__Flammeovirgaceae, g__A4,714990,1000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales, f__Flexibacteraceae, g__Emticicia,146568,1000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales, f__Flexibacteraceae, g__Emticicia,584157,1000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales, f__Flexibacteraceae, g__Spirosoma,4244621,1000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales, f__Flexibacteraceae, g__Spirosoma,denovo1599,1000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales, f__Flexibacteraceae, g__Spirosoma,denovo1895,1000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales, f__Flexibacteraceae, g__Spirosoma,denovo2630,6000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales, f__Saprospiraceae, g__,denovo2048,1000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales, f__Saprospiraceae, g__Haliscomenobacter,76801,1000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales, f__Sphingobacteriaceae, g__,181246,1000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales,,,denovo1445,1000
life,k__Bacteria, p__Bacteroidetes, c__Sphingobacteriia, o__Sphingobacteriales,,,denovo1874,1000
life,k__Bacteria, p__Bacteroidetes,,,,,852920,1000
life,k__Bacteria, p__Bacteroidetes,,,,,denovo1925,1000
life,k__Bacteria, p__Bacteroidetes,,,,,denovo1953,1000
life,k__Bacteria, p__Chlamydiae, c__Chlamydiia, o__Chlamydiales,,,denovo2608,1000
life,k__Bacteria, p__Chlorobi, c__BSV26, o__A89, f__, g__,denovo1444,1000
life,k__Bacteria, p__Chlorobi, c__BSV26, o__A89, f__, g__,denovo286,1000
life,k__Bacteria, p__Chlorobi, c__BSV26, o__PK329, f__, g__,denovo51,1000
life,k__Bacteria, p__Chlorobi, c__Chlorobia, o__Chlorobiales, f__Chlorobiaceae, g__,148055,2000
life,k__Bacteria, p__Chlorobi, c__Chlorobia, o__Chlorobiales, f__Chlorobiaceae,,denovo1822,1000
life,k__Bacteria, p__Chlorobi, c__Ignavibacteria, o__Ignavibacteriales, f__, g__,100928,1000
life,k__Bacteria, p__Chlorobi, c__Ignavibacteria, o__Ignavibacteriales, f__, g__,1109817,1000
life,k__Bacteria, p__Chlorobi, c__Ignavibacteria, o__Ignavibacteriales, f__Ignavibacteriaceae, g__,149540,2000
life,k__Bacteria, p__Chlorobi, c__Ignavibacteria, o__Ignavibacteriales,,,denovo1125,1000
life,k__Bacteria, p__Chlorobi, c__OPB56, o__, f__, g__,822814,1000
life,k__Bacteria, p__Chlorobi, c__OPB56, o__, f__, g__,denovo880,1000
life,k__Bacteria, p__Chloroflexi, c__Anaerolineae, o__Anaerolineales, f__Anaerolinaceae, g__Anaerolinea,143935,1000
life,k__Bacteria, p__Chloroflexi, c__Anaerolineae, o__Anaerolineales, f__Anaerolinaceae, g__Anaerolinea,denovo2394,1000
life,k__Bacteria, p__Chloroflexi, c__Anaerolineae, o__envOPS12, f__, g__,533097,1000
life,k__Bacteria, p__Chloroflexi, c__Anaerolineae, o__envOPS12, f__, g__,1118641,1000
life,k__Bacteria, p__Chloroflexi, c__Anaerolineae, o__H39, f__, g__,denovo2118,1000
life,k__Bacteria, p__Chloroflexi, c__Anaerolineae, o__H39, f__, g__,denovo487,1000
life,k__Bacteria, p__Chloroflexi, c__Anaerolineae,,,,denovo2715,1000
life,k__Bacteria, p__Chloroflexi, c__Chloroflexi, o__, f__, g__,162705,3000
life,k__Bacteria, p__Chloroflexi, c__Chloroflexi, o__Chloroflexales, f__Chloroflexaceae, g__,denovo41,1000
life,k__Bacteria, p__Chloroflexi, c__Ellin6529, o__, f__, g__,82007,1000
life,k__Bacteria, p__Cyanobacteria, c__Chloroplast, o__Stramenopiles, f__, g__,317794,1000
life,k__Bacteria, p__Cyanobacteria, c__Chloroplast, o__Stramenopiles, f__, g__,2257132,3000
life,k__Bacteria, p__Cyanobacteria, c__Chloroplast, o__Stramenopiles, f__, g__,denovo2190,24000
life,k__Bacteria, p__Cyanobacteria, c__Chloroplast, o__Streptophyta, f__, g__,denovo1218,1000
life,k__Bacteria, p__Cyanobacteria, c__Nostocophycideae, o__Nostocales, f__Scytonemataceae, g__,185766,1000
life,k__Bacteria, p__Cyanobacteria, c__Oscillatoriophycideae, o__, f__, g__,denovo2222,7000
life,k__Bacteria, p__Fibrobacteres, c__TG3, o__TG3-1, f__, g__,denovo167,1000
life,k__Bacteria, p__Firmicutes, c__Bacilli, o__, f__, g__,275582,3000
life,k__Bacteria, p__Firmicutes, c__Bacilli, o__Bacillales, f__Paenibacillaceae, g__Paenibacillus,14363,1000
life,k__Bacteria, p__Firmicutes, c__Bacilli, o__Bacillales, f__Paenibacillaceae,,685917,1000
life,k__Bacteria, p__Firmicutes, c__Bacilli, o__Bacillales, f__Planococcaceae,,264748,1000
life,k__Bacteria, p__Firmicutes, c__Bacilli, o__Lactobacillales, f__Aerococcaceae, g__Aerococcus,346565,1000
life,k__Bacteria, p__Firmicutes, c__Clostridia, o__Clostridiales, f__Clostridiaceae, g__,1102185,1000
life,k__Bacteria, p__Firmicutes, c__Clostridia, o__Clostridiales, f__Clostridiaceae, g__Caloramator,denovo1552,1000
life,k__Bacteria, p__Firmicutes, c__Clostridia, o__Clostridiales, f__Clostridiaceae, g__Clostridium,537375,2000
life,k__Bacteria, p__Firmicutes, c__Clostridia, o__Clostridiales, f__Clostridiaceae, g__Clostridium,3876673,1000
life,k__Bacteria, p__Firmicutes, c__Clostridia, o__Clostridiales, f__Clostridiaceae, g__Clostridium,688831,2000
life,k__Bacteria, p__Firmicutes, c__Clostridia, o__Clostridiales, f__Dehalobacteriaceae, g__Dehalobacterium,denovo1405,1000
life,k__Bacteria, p__Firmicutes, c__Clostridia, o__Clostridiales, f__Ruminococcaceae, g__,denovo1379,2000
life,k__Bacteria, p__Firmicutes, c__Clostridia, o__Clostridiales, f__Ruminococcaceae,,718320,1000
life,k__Bacteria, p__Firmicutes, c__Clostridia, o__Clostridiales, f__Ruminococcaceae,,817995,1000
life,k__Bacteria, p__Firmicutes, c__Clostridia, o__Clostridiales, f__Ruminococcaceae,,1115958,2000
life,k__Bacteria, p__Firmicutes, c__Clostridia, o__Clostridiales, f__Syntrophomonadaceae, g__Syntrophomonas,988358,1000
life,k__Bacteria, p__Firmicutes, c__Clostridia, o__Clostridiales, f__Veillonellaceae,,210896,1000
life,k__Bacteria, p__Firmicutes, c__Clostridia, o__Clostridiales,,,824028,1000
life,k__Bacteria, p__Firmicutes, c__Clostridia, o__Clostridiales,,,denovo2527,1000
life,k__Bacteria, p__Firmicutes, c__Clostridia, o__Clostridiales,,,denovo2922,1000
life,k__Bacteria, p__Firmicutes, c__Clostridia, o__Coriobacteriales, f__Coriobacteriaceae, g__,denovo1047,1000
life,k__Bacteria, p__Fusobacteria, c__Fusobacteria, o__Fusobacteriales, f__, g__,2990433,2000
life,k__Bacteria, p__Gemmatimonadetes, c__Gemmatimonadetes, o__Gemmatimonadales, f__Gemmatimonadaceae, g__Gemmatimonas,denovo1472,1000
life,k__Bacteria, p__GN02, c__BD1-5, o__, f__, g__,denovo1288,1000
life,k__Bacteria, p__OD1, c__, o__, f__, g__,denovo2924,1000
life,k__Bacteria, p__OD1, c__ABY1, o__, f__, g__,denovo623,2000
life,k__Bacteria, p__OD1, c__SM2F11, o__, f__, g__,denovo1837,1000
life,k__Bacteria, p__OP3, c__koll11, o__GIF10, f__kpj58rc, g__,denovo2075,1000
life,k__Bacteria, p__Planctomycetes, c__Phycisphaerae, o__, f__, g__,denovo708,1000
life,k__Bacteria, p__Planctomycetes, c__Pla3, o__, f__, g__,509051,1000
life,k__Bacteria, p__Planctomycetes, c__vadinHA49, o__DH61, f__, g__,denovo2893,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Caulobacterales, f__Caulobacteraceae, g__Caulobacter,128790,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Caulobacterales, f__Caulobacteraceae, g__Phenylobacterium,5512,2000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Ellin329, f__, g__,denovo1816,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhizobiales, f__Bradyrhizobiaceae,,216805,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhizobiales, f__Brucellaceae, g__Ochrobactrum,290517,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhizobiales, f__Brucellaceae,,534015,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhizobiales, f__Hyphomicrobiaceae, g__Devosia,144645,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhizobiales, f__Hyphomicrobiaceae, g__Rhodoplanes,744505,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhizobiales, f__Hyphomicrobiaceae, g__Rhodoplanes,2972756,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhizobiales, f__Methylobacteriaceae, g__,237302,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhizobiales, f__Methylobacteriaceae, g__Methylobacterium,258707,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhizobiales, f__Methylobacteriaceae, g__Methylobacterium,579710,2000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhizobiales, f__Methylocystaceae, g__,136235,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhizobiales, f__Rhizobiaceae, g__,574749,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhizobiales, f__Rhizobiaceae, g__Agrobacterium,128628,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhizobiales, f__Rhizobiaceae, g__Agrobacterium,220269,2000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhizobiales, f__Rhizobiaceae,,578761,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhizobiales, f__Rhodobiaceae, g__,251598,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhizobiales,,,225511,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhizobiales,,,229404,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhizobiales,,,256527,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhizobiales,,,513366,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhizobiales,,,751360,2000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhodobacterales, f__Hyphomonadaceae, g__,519257,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhodobacterales, f__Rhodobacteraceae, g__Rhodobacter,267759,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhodobacterales, f__Rhodobacteraceae, g__Rhodobacter,683891,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhodobacterales, f__Rhodobacteraceae, g__Rhodobacter,704995,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhodobacterales, f__Rhodobacteraceae, g__Rhodobacter,746799,4000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhodospirillales, f__, g__,246860,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhodospirillales, f__Acetobacteraceae, g__,denovo2073,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhodospirillales, f__Acetobacteraceae, g__Roseomonas,75850,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhodospirillales, f__Rhodospirillaceae, g__Azospirillum,115023,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhodospirillales, f__Rhodospirillaceae, g__Telmatospirillum,93710,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhodospirillales, f__Rhodospirillaceae, g__Telmatospirillum,denovo2065,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhodospirillales, f__Rhodospirillaceae, g__Telmatospirillum,denovo882,2000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhodospirillales, f__Rhodospirillaceae, g__Telmatospirillum,denovo214,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rhodospirillales, f__Rhodospirillaceae,,554299,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rickettsiales, f__, g__,277868,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rickettsiales, f__mitochondria, g__,denovo130,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rickettsiales, f__mitochondria, g__,denovo1570,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rickettsiales, f__mitochondria, g__,denovo1747,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rickettsiales, f__mitochondria, g__,denovo2059,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rickettsiales, f__mitochondria, g__,denovo2615,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rickettsiales, f__mitochondria, g__,denovo508,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rickettsiales, f__mitochondria, g__,denovo690,2000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Rickettsiales, f__mitochondria, g__,denovo950,2000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Sphingomonadales, f__Erythrobacteraceae,,1083099,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Sphingomonadales, f__Sphingomonadaceae, g__Kaistobacter,145518,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Sphingomonadales, f__Sphingomonadaceae, g__Kaistobacter,203846,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Sphingomonadales, f__Sphingomonadaceae, g__Kaistobacter,246578,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Sphingomonadales, f__Sphingomonadaceae, g__Kaistobacter,307166,4000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Sphingomonadales, f__Sphingomonadaceae, g__Kaistobacter,denovo2260,6000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Sphingomonadales, f__Sphingomonadaceae, g__Novosphingobium,72153,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Sphingomonadales, f__Sphingomonadaceae, g__Novosphingobium,133044,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Sphingomonadales, f__Sphingomonadaceae, g__Novosphingobium,231088,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Sphingomonadales, f__Sphingomonadaceae, g__Sphingobium,105198,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Sphingomonadales, f__Sphingomonadaceae, g__Sphingomonas,152429,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Sphingomonadales, f__Sphingomonadaceae, g__Sphingomonas,588052,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Sphingomonadales, f__Sphingomonadaceae, g__Sphingomonas,838293,2000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Sphingomonadales, f__Sphingomonadaceae, g__Sphingomonas,149563,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Sphingomonadales, f__Sphingomonadaceae, g__Sphingomonas,354042,2000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Sphingomonadales, f__Sphingomonadaceae,,552687,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Sphingomonadales, f__Sphingomonadaceae,,1114792,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Sphingomonadales, f__Sphingomonadaceae,,denovo1197,2000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria, o__Sphingomonadales, f__Sphingomonadaceae,,denovo2304,8000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria,,,,357011,1000
life,k__Bacteria, p__Proteobacteria, c__Alphaproteobacteria,,,,denovo66,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Alcaligenaceae, g__Achromobacter,423327,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae, g__Aquabacterium,1107819,2000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae, g__Comamonas,295086,4000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae, g__Comamonas,3796550,7000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae, g__Hydrogenophaga,47512,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae, g__Hydrogenophaga,97176,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae, g__Hydrogenophaga,102445,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae, g__Hydrogenophaga,136160,3000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae, g__Hydrogenophaga,144875,5000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae, g__Hydrogenophaga,552978,8000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae, g__Hydrogenophaga,829669,23000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae, g__Hylemonella,821548,22000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae, g__Limnohabitans,308944,8000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae, g__Limnohabitans,343284,20000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae, g__Rubrivivax,115156,3000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae, g__Rubrivivax,166838,4000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae, g__Rubrivivax,4170464,9000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,6997,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,7043,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,43597,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,74685,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,84980,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,93726,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,98380,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,106999,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,110852,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,113128,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,137411,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,143487,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,147885,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,160195,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,164959,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,172053,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,204526,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,215539,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,236168,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,245121,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,249150,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,261931,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,264669,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,281172,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,310563,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,317724,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,323551,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,338208,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,348395,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,351940,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,394369,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,412392,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,463546,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,510711,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,545507,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,545956,2000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,545997,2000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,553551,2000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,554158,2000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,585904,2000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,587796,2000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,651074,2000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,664656,2000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,696865,2000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,699206,2000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,750840,2000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,764906,2000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,765165,3000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,818509,3000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,821566,3000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,834682,3000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,841724,3000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,846329,3000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,1116348,3000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,1124268,3000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,1124681,4000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,1125869,4000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,1131789,4000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,1137143,4000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,1148287,4000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,2194872,4000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,2792176,5000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,2792177,5000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,4254478,6000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,denovo1378,7000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,denovo1838,10000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,denovo2355,13000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,denovo2358,37000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,denovo2769,41000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,denovo2956,48000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,denovo641,81000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Comamonadaceae,,denovo916,102000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Oxalobacteraceae, g__,247545,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Oxalobacteraceae, g__Janthinobacterium,358564,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Oxalobacteraceae, g__Polynucleobacter,352838,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Oxalobacteraceae,,227265,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales, f__Oxalobacteraceae,,581409,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales,,,3006054,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales,,,4091428,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales,,,denovo2803,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales,,,denovo549,2000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Burkholderiales,,,denovo562,9000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Ellin6067, f__, g__,1127926,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Gallionellales, f__Gallionellaceae, g__Gallionella,1147713,2000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Hydrogenophilales, f__Hydrogenophilaceae, g__Thiobacillus,786890,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Methylophilales, f__Methylophilaceae, g__,264040,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Methylophilales, f__Methylophilaceae, g__,821712,15000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Methylophilales, f__Methylophilaceae, g__Methylotenera,509174,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Methylophilales, f__Methylophilaceae, g__Methylotenera,520725,2000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Methylophilales, f__Methylophilaceae, g__Methylotenera,541424,5000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Methylophilales, f__Methylophilaceae, g__Methylotenera,114612,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Methylophilales, f__Methylophilaceae, g__Methylotenera,305721,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Methylophilales, f__Methylophilaceae,,142762,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Methylophilales, f__Methylophilaceae,,denovo2207,2000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Methylophilales,,,1117946,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Neisseriales, f__Neisseriaceae,,denovo2102,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Rhodocyclales, f__Rhodocyclaceae, g__,365866,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Rhodocyclales, f__Rhodocyclaceae, g__Azospira,163897,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Rhodocyclales, f__Rhodocyclaceae, g__Dechloromonas,149111,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Rhodocyclales, f__Rhodocyclaceae, g__Dechloromonas,592056,4000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Rhodocyclales, f__Rhodocyclaceae, g__Dechloromonas,783508,5000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Rhodocyclales, f__Rhodocyclaceae, g__Dechloromonas,1136953,12000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Rhodocyclales, f__Rhodocyclaceae, g__Sulfuritalea,224877,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Rhodocyclales, f__Rhodocyclaceae, g__Uliginosibacterium,168182,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Rhodocyclales, f__Rhodocyclaceae, g__Zoogloea,584010,2000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Rhodocyclales, f__Rhodocyclaceae,,6673,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Rhodocyclales, f__Rhodocyclaceae,,142103,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Rhodocyclales, f__Rhodocyclaceae,,511887,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Rhodocyclales, f__Rhodocyclaceae,,516341,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Rhodocyclales, f__Rhodocyclaceae,,536858,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Rhodocyclales, f__Rhodocyclaceae,,586984,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Rhodocyclales, f__Rhodocyclaceae,,759257,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Rhodocyclales, f__Rhodocyclaceae,,805571,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Rhodocyclales, f__Rhodocyclaceae,,1115299,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Rhodocyclales, f__Rhodocyclaceae,,2451651,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Rhodocyclales, f__Rhodocyclaceae,,2891957,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Rhodocyclales, f__Rhodocyclaceae,,denovo1120,2000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Rhodocyclales, f__Rhodocyclaceae,,denovo2382,22000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__SBla14, f__, g__,341843,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__SC-I-84, f__, g__,238426,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria, o__Thiobacterales, f__, g__,1112811,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria,,,,6752,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria,,,,137480,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria,,,,143135,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria,,,,170130,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria,,,,178053,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria,,,,240233,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria,,,,245670,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria,,,,562860,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria,,,,567753,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria,,,,3116300,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria,,,,denovo1004,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria,,,,denovo1431,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria,,,,denovo1708,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria,,,,denovo1720,1000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria,,,,denovo2274,2000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria,,,,denovo2284,2000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria,,,,denovo2695,2000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria,,,,denovo422,2000
life,k__Bacteria, p__Proteobacteria, c__Betaproteobacteria,,,,denovo984,8000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__, f__, g__,308373,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__, f__, g__,554266,3000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Bdellovibrionales, f__Bacteriovoracaceae, g__,809317,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Bdellovibrionales, f__Bacteriovoracaceae, g__,denovo2039,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Bdellovibrionales, f__Bacteriovoracaceae, g__,denovo2122,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Bdellovibrionales, f__Bacteriovoracaceae, g__,denovo834,10000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Desulfobacterales, f__Desulfobulbaceae, g__,276287,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Desulfobacterales, f__Desulfobulbaceae, g__Desulfobulbus,247260,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Desulfovibrionales, f__Desulfovibrionaceae, g__Desulfovibrio,592620,2000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Desulfovibrionales, f__Desulfovibrionaceae, g__Desulfovibrio,denovo3021,2000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Desulfovibrionales,,,denovo964,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Desulfurellales, f__, g__,840765,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Desulfuromonadales, f__Geobacteraceae, g__Geobacter,48355,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Desulfuromonadales, f__Geobacteraceae, g__Geobacter,202514,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Desulfuromonadales, f__Geobacteraceae, g__Geobacter,635511,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Desulfuromonadales, f__Geobacteraceae, g__Geobacter,1140968,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Desulfuromonadales, f__Geobacteraceae,,110735,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Desulfuromonadales, f__Geobacteraceae,,1115527,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Desulfuromonadales,,,220762,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Desulfuromonadales,,,denovo304,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Desulfuromonadales,,,denovo738,4000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Myxococcales, f__, g__,1002966,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Myxococcales, f__0319-6G20, g__,771634,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Myxococcales, f__Cystobacteraceae, g__Cystobacter,denovo1157,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Myxococcales, f__Cystobacteraceae,,336745,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Myxococcales, f__Nannocystaceae, g__Nannocystis,314203,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Myxococcales, f__Nannocystaceae, g__Plesiocystis,3992505,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Myxococcales,,,501684,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Myxococcales,,,denovo177,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Myxococcales,,,denovo2251,2000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Spirobacillales, f__, g__,denovo1665,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Syntrophobacterales, f__Syntrophaceae, g__Syntrophus,612227,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Syntrophobacterales, f__Syntrophaceae, g__Syntrophus,670053,2000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Syntrophobacterales, f__Syntrophaceae,,denovo429,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Syntrophobacterales, f__Syntrophobacteraceae, g__Syntrophobacter,163774,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Syntrophobacterales, f__Syntrophobacteraceae, g__Syntrophobacter,denovo2809,1000
life,k__Bacteria, p__Proteobacteria, c__Deltaproteobacteria, o__Syntrophobacterales, f__Syntrophorhabdaceae, g__,143834,1000
life,k__Bacteria, p__Proteobacteria, c__Epsilonproteobacteria, o__Campylobacterales, f__Campylobacteraceae, g__Arcobacter,144024,3000
life,k__Bacteria, p__Proteobacteria, c__Epsilonproteobacteria, o__Campylobacterales, f__Helicobacteraceae, g__,denovo879,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Aeromonadales, f__Aeromonadaceae, g__,164822,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Aeromonadales, f__Aeromonadaceae, g__,203157,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Aeromonadales, f__Aeromonadaceae, g__Tolumonas,526817,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Aeromonadales,,,denovo1492,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Alteromonadales, f__[Chromatiaceae], g__Rheinheimera,139424,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Alteromonadales, f__Alteromonadaceae, g__Cellvibrio,819023,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Enterobacteriales, f__Enterobacteriaceae, g__Morganella,720489,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Enterobacteriales, f__Enterobacteriaceae, g__Providencia,365184,6000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Enterobacteriales, f__Enterobacteriaceae,,54877,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Enterobacteriales, f__Enterobacteriaceae,,569979,2000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Legionellales, f__Coxiellaceae, g__,denovo2702,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Legionellales, f__Coxiellaceae, g__Aquicella,232046,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Legionellales,,,612198,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Legionellales,,,denovo2953,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Crenotrichaceae, g__Crenothrix,131019,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Crenotrichaceae, g__Crenothrix,534688,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Crenotrichaceae, g__Crenothrix,2400244,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Crenotrichaceae, g__Crenothrix,2400246,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Crenotrichaceae, g__Crenothrix,3638246,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Crenotrichaceae, g__Crenothrix,denovo1344,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Crenotrichaceae, g__Crenothrix,denovo1796,2000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Crenotrichaceae, g__Crenothrix,denovo1804,3000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Crenotrichaceae, g__Crenothrix,denovo203,10000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Crenotrichaceae, g__Crenothrix,denovo2074,11000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Crenotrichaceae, g__Crenothrix,denovo2227,20000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Crenotrichaceae, g__Crenothrix,denovo354,27000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Crenotrichaceae, g__Crenothrix,denovo357,82000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Crenotrichaceae, g__Crenothrix,denovo936,218000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Crenotrichaceae, g__Crenothrix,3219860,2000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Crenotrichaceae, g__Crenothrix,denovo1201,8000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Crenotrichaceae, g__Crenothrix,denovo146,13000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Crenotrichaceae, g__Crenothrix,denovo1850,36000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Crenotrichaceae, g__Crenothrix,denovo1922,36000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Methylococcaceae, g__,denovo1116,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Methylococcaceae, g__Methylocaldum,380204,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Methylococcaceae, g__Methylocaldum,denovo2386,2000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Methylococcaceae, g__Methylomonas,8057,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Methylococcaceae, g__Methylomonas,8067,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Methylococcaceae, g__Methylomonas,8090,2000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Methylococcaceae, g__Methylomonas,40125,4000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Methylococcaceae, g__Methylomonas,45263,5000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Methylococcaceae, g__Methylomonas,142784,9000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Methylococcaceae, g__Methylomonas,588559,23000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Methylococcaceae,,141872,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Methylococcaceae,,1124243,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Methylococcaceae,,denovo1643,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Methylococcaceae,,denovo1691,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Methylococcaceae,,denovo2135,2000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales, f__Methylococcaceae,,denovo893,7000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales,,,denovo1510,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales,,,denovo2188,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales,,,denovo2330,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales,,,denovo2544,2000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Methylococcales,,,denovo2653,7000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Pseudomonadales, f__Moraxellaceae, g__Acinetobacter,54545,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Pseudomonadales, f__Moraxellaceae, g__Acinetobacter,579115,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Pseudomonadales, f__Moraxellaceae, g__Acinetobacter,194118,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Pseudomonadales, f__Moraxellaceae, g__Acinetobacter,532598,4000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Pseudomonadales, f__Moraxellaceae, g__Acinetobacter,286025,3000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Pseudomonadales, f__Moraxellaceae, g__Acinetobacter,388951,4000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Pseudomonadales, f__Moraxellaceae, g__Enhydrobacter,484436,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Pseudomonadales, f__Moraxellaceae, g__Enhydrobacter,denovo2344,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Pseudomonadales, f__Moraxellaceae,,548754,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Pseudomonadales, f__Pseudomonadaceae, g__Pseudomonas,72643,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Pseudomonadales, f__Pseudomonadaceae, g__Pseudomonas,400315,2000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Pseudomonadales, f__Pseudomonadaceae, g__Pseudomonas,179854,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Pseudomonadales, f__Pseudomonadaceae, g__Pseudomonas,394796,2000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Pseudomonadales, f__Pseudomonadaceae, g__Pseudomonas,410048,45000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Pseudomonadales, f__Pseudomonadaceae,,156652,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Pseudomonadales, f__Pseudomonadaceae,,denovo793,3000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Xanthomonadales, f__Sinobacteraceae, g__Nevskia,3120500,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Xanthomonadales, f__Xanthomonadaceae, g__Lysobacter,2340272,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Xanthomonadales, f__Xanthomonadaceae, g__Rhodanobacter,179061,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria, o__Xanthomonadales, f__Xanthomonadaceae,,449595,3000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,7505,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,897420,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,denovo11,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,denovo1117,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,denovo118,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,denovo1410,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,denovo1488,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,denovo1616,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,denovo170,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,denovo1750,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,denovo2093,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,denovo2258,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,denovo2296,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,denovo2573,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,denovo2587,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,denovo2785,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,denovo2921,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,denovo2954,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,denovo603,1000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,denovo654,2000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,denovo767,2000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,denovo897,6000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,denovo908,8000
life,k__Bacteria, p__Proteobacteria, c__Gammaproteobacteria,,,,denovo94,91000
life,k__Bacteria, p__Proteobacteria,,,,,denovo1107,1000
life,k__Bacteria, p__Proteobacteria,,,,,denovo2144,1000
life,k__Bacteria, p__Spirochaetes, c__[Brevinematae], o__[Brevinematales], f__, g__,2347450,1000
life,k__Bacteria, p__Spirochaetes, c__[Leptospirae], o__[Leptospirales], f__Leptospiraceae, g__,denovo666,1000
life,k__Bacteria, p__Spirochaetes, c__[Leptospirae], o__[Leptospirales], f__Sediment-4, g__SJA-88,317015,1000
life,k__Bacteria, p__Spirochaetes, c__[Leptospirae], o__[Leptospirales], f__Sediment-4, g__SJA-88,1108618,1000
life,k__Bacteria, p__Spirochaetes, c__[Leptospirae], o__[Leptospirales], f__Sediment-4, g__SJA-88,denovo1776,2000
life,k__Bacteria, p__Spirochaetes, c__Spirochaetes, o__Spirochaetales, f__Spirochaetaceae, g__Spirochaeta,89319,1000
life,k__Bacteria, p__TM7, c__SC3, o__, f__, g__,denovo1069,1000
life,k__Bacteria, p__Verrucomicrobia, c__[Pedosphaerae], o__[Pedosphaerales], f__, g__,610383,1000
life,k__Bacteria, p__Verrucomicrobia, c__[Pedosphaerae], o__[Pedosphaerales], f__, g__,denovo408,1000
life,k__Bacteria, p__Verrucomicrobia, c__[Pedosphaerae], o__[Pedosphaerales], f__auto67_4W, g__,813303,1000
life,k__Bacteria, p__Verrucomicrobia, c__[Pedosphaerae], o__[Pedosphaerales], f__auto67_4W, g__,1120116,1000
life,k__Bacteria, p__Verrucomicrobia, c__[Pedosphaerae], o__[Pedosphaerales], f__auto67_4W, g__,2409043,1000
life,k__Bacteria, p__Verrucomicrobia, c__[Pedosphaerae], o__[Pedosphaerales], f__auto67_4W, g__,denovo1198,2000
life,k__Bacteria, p__Verrucomicrobia, c__[Pedosphaerae], o__[Pedosphaerales], f__Ellin515, g__,1105298,1000
life,k__Bacteria, p__Verrucomicrobia, c__[Pedosphaerae], o__[Pedosphaerales], f__Ellin515, g__,denovo42,1000
life,k__Bacteria, p__Verrucomicrobia, c__[Pedosphaerae], o__[Pedosphaerales],,,denovo1025,1000
life,k__Bacteria, p__Verrucomicrobia, c__[Pedosphaerae], o__[Pedosphaerales],,,denovo1303,2000
life,k__Bacteria, p__Verrucomicrobia, c__[Pedosphaerae],,,,denovo2463,1000
life,k__Bacteria, p__Verrucomicrobia, c__[Spartobacteria], o__[Chthoniobacterales], f__[Chthoniobacteraceae], g__Ellin506,denovo1442,1000
life,k__Bacteria, p__Verrucomicrobia, c__Opitutae, o__Opitutales, f__Opitutaceae, g__,697714,1000
life,k__Bacteria, p__Verrucomicrobia, c__Verrucomicrobiae, o__Verrucomicrobiales, f__Verrucomicrobiaceae, g__Prosthecobacter,denovo307,1000
life,k__Bacteria, p__Verrucomicrobia, c__Verrucomicrobiae, o__Verrucomicrobiales, f__Verrucomicrobiaceae,,341698,1000
life,k__Bacteria, p__WYO, c__, o__, f__, g__,688363,1000
life,k__Bacteria, p__WYO, c__, o__, f__, g__,1028542,2000
life,k__Bacteria,,,,,,denovo1014,1000
life,k__Bacteria,,,,,,denovo1111,1000
life,k__Bacteria,,,,,,denovo1149,1000
life,k__Bacteria,,,,,,denovo1249,1000
life,k__Bacteria,,,,,,denovo1371,1000
life,k__Bacteria,,,,,,denovo1418,1000
life,k__Bacteria,,,,,,denovo1501,1000
life,k__Bacteria,,,,,,denovo1515,1000
life,k__Bacteria,,,,,,denovo1630,1000
life,k__Bacteria,,,,,,denovo1740,1000
life,k__Bacteria,,,,,,denovo1851,1000
life,k__Bacteria,,,,,,denovo1952,1000
life,k__Bacteria,,,,,,denovo1972,1000
life,k__Bacteria,,,,,,denovo2053,1000
life,k__Bacteria,,,,,,denovo212,1000
life,k__Bacteria,,,,,,denovo2152,1000
life,k__Bacteria,,,,,,denovo2242,1000
life,k__Bacteria,,,,,,denovo2378,1000
life,k__Bacteria,,,,,,denovo2433,1000
life,k__Bacteria,,,,,,denovo2508,1000
life,k__Bacteria,,,,,,denovo2535,1000
life,k__Bacteria,,,,,,denovo2538,1000
life,k__Bacteria,,,,,,denovo2556,1000
life,k__Bacteria,,,,,,denovo2680,1000
life,k__Bacteria,,,,,,denovo2745,1000
life,k__Bacteria,,,,,,denovo277,1000
life,k__Bacteria,,,,,,denovo2857,1000
life,k__Bacteria,,,,,,denovo2860,1000
life,k__Bacteria,,,,,,denovo2896,1000
life,k__Bacteria,,,,,,denovo2925,1000
life,k__Bacteria,,,,,,denovo312,1000
life,k__Bacteria,,,,,,denovo463,2000
life,k__Bacteria,,,,,,denovo474,3000
life,k__Bacteria,,,,,,denovo488,3000
life,k__Bacteria,,,,,,denovo634,5000
life,k__Bacteria,,,,,,denovo792,6000
life,k__Bacteria,,,,,,denovo929,9000
'''

rows = list(csv.reader(s.splitlines()))
r = json.dumps(cluster(rows),indent = 2)
r = r.split('\n')
r.pop()
r.pop(0)
import string
t = string.join(r,'\n')
data = open('flare.json', 'w')
data.write(t)
data.close()
