# Organização do banco de dados no MONGODB

As questões são separadas de acordo com o ano da prova, em habilidades, em competências e em seções de matérias. Dessa forma, criaremos algumas coleções para organizar todos os dados, que serão: `col_questoes`, `col_provas`, `col_materias`.

## Coleções de questões:

*Col_questão:*
```json
{
    "id_questao":"<int>",
    "numero_questao":"<array_questao>",
    "enunciado": "<string>",
    "alternativas":"<array>",
    "resposta":"<[0,1,2,3,4]>", 
    "habilidades":"<array_habilidades>",
    "competencias":"<array_competencias>",
    "ano":"<int>"
}

```

*Col_num_questao*:

```json
{
    "branco":"<int>",
    "amarelo":"<int>",
    "verde":"<int>",
    "azul":"<int>",
}
```



## Coleções de provas:

```json

{
    "id_prova_ano":"<int>",
    "questoes":"<array_questoes_id:col_questoes>",
}

```