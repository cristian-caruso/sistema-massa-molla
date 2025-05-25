# Simulazione Massa-Molla con Attrito Viscoso

Questo progetto Python simula il moto di una massa attaccata a una molla in presenza di attrito viscoso. Il sistema è descritto da un'equazione differenziale del secondo ordine e viene risolto numericamente tramite un'integrazione diretta.

## Descrizione

Il sistema fisico modellato è quello di una massa **m** attaccata a una molla con costante elastica **k**, soggetta a una forza di attrito viscoso proporzionale alla velocità (**b**). L'equazione differenziale che descrive il moto è:

![Equazione differenziale del moto](https://github.com/user-attachments/assets/d7efbae9-3347-4ecc-bfc6-e09c358ed167)


Il programma:
- Chiede all'utente i parametri `m`, `k`, `b` e l'ampiezza iniziale.
- Esegue la simulazione numerica usando un passo di integrazione costante.
- Calcola posizione, velocità e accelerazione a ogni intervallo di tempo.
- Mostra un grafico della posizione in funzione del tempo.

## Dipendenze

- Python 3
- matplotlib

Installa le dipendenze con:

```bash
pip install matplotlib
```

## Output
Il programma genera un grafico della posizione nel tempo, mostrando l'oscillazione smorzata del sistema.

## Autore
Cristian Caruso

## Licenza
Distribuito con licenza MIT.
