#정규표현식 Regular Expression
    정규 표현식은 특정한 규칙을 가진 문자열의 패턴을 표현하는데 사용하는 표현식이다.
    파이썬에서는 re 모듈을 통해 보통 사용하는듯?
    메타문자 : . ^ $ * + ? { } [ ] \ | ( )

    [ ] <- [ ] 사이의 문자들과 매치 라는 의미를 갖고있다.
    [abc] -> a,b,c 중 한개의 문자와 매치를 뜻함.
    [a-zA-Z] -> 알파벳 모두를 뜻함  -는 From - to를 의미.
    ^ <- not이라는 의미를 갖고있다. 예를들어
    [^0-9] -> 숫자가 아닌 문자만 매치된다.

    . <- 줄바꿈 문자를 제외한 모든 문자와 매치됨을 의미.
    a.b -> "a + 모든문자 + b"

    * <- 반복
    ca*t -> ct, cat , caat, caat, caaaaat등과 모두 매치.

    + <- 반복을 나타내는 문자. +는 최소 1번이상 반복할때 사용 
    ca+t -> ct (x) cat(o) , caaat(o)

    