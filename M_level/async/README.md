# asyncio

* asyncio는 비동기 프로그래밍을 위한 모듈
    CPU작업과 I/O를 병렬로 처리 가능하게 해준다

* 동기 처리와의 비교
    동기 처리는 특정 작업이 끝나면 다음 작업을 처리하는 순차 처리
    비동기 처리는 여러 작업을 처리하도록 예약한 뒤 작업 후 결과 받는 방식

* 네이티브 코루틴과 제네레이터 기반 코루틴

```python3
async def func():
    pass #do something
```

``` python3
import asyncio
 
async def hello():    # async def로 네이티브 코루틴을 만듦
    print('Hello, world!')
 
loop = asyncio.get_event_loop()     # 이벤트 루프를 얻음
loop.run_until_complete(hello())    # hello가 끝날 때까지 기다림
loop.close()   
```

` async def` 로 함수를 만들 수 있다.