from .models import Product
from .models import StepProduct


def PopulateDb():
    pr1 = Product(
        name="Carne di pollo sintetica",
        description="questa è la descrizione della Carne di pollo sintetica",
    )
    pr1.save()
    sp1 = StepProduct(
        description="PASSAGGIO  1\n Campione \n Le cellule sono gli elementi costitutivi della carne, quindi identifichiamo e selezioniamo i polli migliori per darci le cellule ideali per una carne dal sapore eccezionale.\n\nPollo allevato a terra a Piacenza",
        code=pr1.code,
    )
    sp1.save()
    sp2 = StepProduct(
        description="PASSAGGIO  2\n Nutrire \n Per produrre carne di pollo, dobbiamo prima nutrire le cellule. Diamo loro da mangiare una miscela brevettata di micronutrienti ottimizzati per le nostre carni.\n\nLaboratorio di Milano",
        code=pr1.code,
    )
    sp2.save()
    sp3 = StepProduct(
        description="PASSAGGIO  3\n Coltivare \n Mettiamo le cellule in una nave chiamata coltivatore. Lì seguono il loro processo naturale per formare la carne, proprio come farebbero su un animale.\n\nLaboratorio di Milano",
        code=pr1.code,
    )
    sp3.save()
    sp4 = StepProduct(
        description="PASSAGGIO  4\n Raccolto \n Dopo 22 giorni abbiamo raccolto la carne. Pronto per essere ispezionato, preparato, confezionato, servito e gustato.\n\nMesso in vendita sul nostro sito",
        code=pr1.code,
    )
    sp4.save()

    pr2 = Product(
        name="Carne di manzo sintetica",
        description="questa è la descrizione della Carne di manzo sintetica",
    )
    pr2.save()
    sp21 = StepProduct(
        description="PASSAGGIO  1\n Campione \n Le cellule sono gli elementi costitutivi della carne, quindi identifichiamo e selezioniamo i bovini migliori per darci le cellule ideali per una carne dal sapore eccezionale.\n\nManzo allevato in pascoli a Treviso",
        code=pr2.code,
    )
    sp21.save()
    sp22 = StepProduct(
        description="PASSAGGIO  2\n Nutrire \n Per produrre carne di manzo, dobbiamo prima nutrire le cellule. Diamo loro da mangiare una miscela brevettata di micronutrienti ottimizzati per le nostre carni.\n\nLaboratorio di Milano",
        code=pr2.code,
    )
    sp22.save()
    sp23 = StepProduct(
        description="PASSAGGIO  3\n Coltivare \n Mettiamo le cellule in una nave chiamata coltivatore. Lì seguono il loro processo naturale per formare la carne, proprio come farebbero su un animale.\n\nLaboratorio di Milano",
        code=pr2.code,
    )
    sp23.save()
    sp24 = StepProduct(
        description="PASSAGGIO  4\n Raccolto \n Dopo 18 giorni abbiamo raccolto la carne. Pronto per essere ispezionato, preparato, confezionato, servito e gustato.\n\nMesso in vendita sul nostro sito",
        code=pr2.code,
    )
    sp24.save()

    pr3 = Product(
        name="Carne di mucca sintetica",
        description="questa è la descrizione della Carne di mucca sintetica",
    )
    pr3.save()
    sp31 = StepProduct(
        description="PASSAGGIO  1\n Campione \n Le cellule sono gli elementi costitutivi della carne, quindi identifichiamo e selezioniamo le mucche migliori per darci le cellule ideali per una carne dal sapore eccezionale.\n\nMucche allevate in pascoli in Valle Stura",
        code=pr3.code,
    )
    sp31.save()
    sp32 = StepProduct(
        description="PASSAGGIO  2\n Nutrire \n Per produrre carne di mucca, dobbiamo prima nutrire le cellule. Diamo loro da mangiare una miscela brevettata di micronutrienti ottimizzati per le nostre carni.\n\nLaboratorio di Milano",
        code=pr3.code,
    )
    sp32.save()
    sp33 = StepProduct(
        description="PASSAGGIO  3\n Coltivare \n Mettiamo le cellule in una nave chiamata coltivatore. Lì seguono il loro processo naturale per formare la carne, proprio come farebbero su un animale.\n\nLaboratorio di Milano",
        code=pr3.code,
    )
    sp33.save()
    sp34 = StepProduct(
        description="PASSAGGIO  4\n Raccolto \n Dopo 25 giorni abbiamo raccolto la carne. Pronto per essere ispezionato, preparato, confezionato, servito e gustato.\n\nMesso in vendita sul nostro sito",
        code=pr3.code,
    )
    sp34.save()

    pr4 = Product(
        name="Carne di tacchino sintetica",
        description="questa è la descrizione della Carne di tacchino sintetica",
    )
    pr4.save()
    sp41 = StepProduct(
        description="PASSAGGIO  1\n Campione \n Le cellule sono gli elementi costitutivi della carne, quindi identifichiamo e selezioniamo i tacchini migliori per darci le cellule ideali per una carne dal sapore eccezionale.\n\tacchino allevati a terra a Bronzato",
        code=pr4.code,
    )
    sp41.save()
    sp42 = StepProduct(
        description="PASSAGGIO  2\n Nutrire \n Per produrre carne di tacchino, dobbiamo prima nutrire le cellule. Diamo loro da mangiare una miscela brevettata di micronutrienti ottimizzati per le nostre carni.\n\nLaboratorio di Milano",
        code=pr4.code,
    )
    sp42.save()
    sp43 = StepProduct(
        description="PASSAGGIO  3\n Coltivare \n Mettiamo le cellule in una nave chiamata coltivatore. Lì seguono il loro processo naturale per formare la carne, proprio come farebbero su un animale.\n\nLaboratorio di Milano",
        code=pr4.code,
    )
    sp43.save()
    sp44 = StepProduct(
        description="PASSAGGIO  4\n Raccolto \n Dopo 19 giorni abbiamo raccolto la carne. Pronto per essere ispezionato, preparato, confezionato, servito e gustato.\n\nMesso in vendita sul nostro sito",
        code=pr4.code,
    )
    sp44.save()
