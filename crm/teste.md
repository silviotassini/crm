``` mermaid
classDiagram
    categ "1" <|-- "*" Question
    Question "1" <|-- "*" Answer
    categ : -int id
    categ : -int text
    categ: +metodo00()

    class Question{
        -int id
        -int categ_id
        +String question
        +int answer_type
        +String info
        +String tags

        Question: +metodo01()
    }

    class Answer{
      -int id
      -int question_id
      +String answer
      +int correct

      +metodo02()
    }

            
```