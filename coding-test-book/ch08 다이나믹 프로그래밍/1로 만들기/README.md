## 문제 내용

- 정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 4가지
  - X가 5로 나누어떨어지면, 5로 나누기
  - X가 3으로 나누어떨어지면, 3으로 나누기
  - X가 2로 나누어떨어지면, 2로 나누기
  - X에서 1을 빼기
- X에 연산 4개를 적절히 사용해서 1을 만들려고 함
- 연산을 사용하는 횟수의 최솟값을 출력

### 입력 조건

- 첫째 줄에 정수 X가 주어짐 $(1 \le x \le 30,000)$

### 출력 조건

- 첫째 줄에 연산을 하는 횟수의 최솟값을 출력

### 입력 예시

``` plain text
26
```

### 출력 예시

``` plain text
3
```

---

## 문제 해설

- 예를 들어, X가 6일 때 함수가 호출되는 과정을 그림으로 나타내면 다음과 같음

[![](https://mermaid.ink/img/pako:eNp90b0KwyAQAOBXCTclkAzRJIOFTlk7taNQJJofWmOwOpSQd6-NWDJInfS-u0PuVugUF0Bg0GwZk1t7onPiTt-kKYU-bTIKWZYUxTnpax-q91BI84Q94Qihe-kRHbH2WHmqIlSGuvKIODRFkaY4VKJIpftHYPyfqyNDDlJoySbuhrR-kymYUUhBgbgrZ_pBgc6by2PWqOt77oAYbUUOWtlhBNKz58u97MKZEe3E3KTlLyr4ZJS--B3sq9g-f9Fn4g?type=png)](https://mermaid.live/edit#pako:eNp90b0KwyAQAOBXCTclkAzRJIOFTlk7taNQJJofWmOwOpSQd6-NWDJInfS-u0PuVugUF0Bg0GwZk1t7onPiTt-kKYU-bTIKWZYUxTnpax-q91BI84Q94Qihe-kRHbH2WHmqIlSGuvKIODRFkaY4VKJIpftHYPyfqyNDDlJoySbuhrR-kymYUUhBgbgrZ_pBgc6by2PWqOt77oAYbUUOWtlhBNKz58u97MKZEe3E3KTlLyr4ZJS--B3sq9g-f9Fn4g)

- $f(2)$와 같은 함수들이 동일하게 여러 번 호출되는 것을 알 수 있음
- 동일한 함수에서 구하는 값들은 동일해야 하므로 다이나믹 프로그래밍을 효과적으로 사용할 수 있음
- 문제에서 요구하는 내용을 점화식으로 표현하면 다음과 같음, 점화식 끝에 1을 더하는 이유는 함수의 호출 횟수를 구해야 하기 때문
$a_i = min(a_{i-1}, a_{i/2}, a_{i/3}, a_{i/5}) + 1$
- 위 점화식을 토대로 바텀업 다이나믹 프로그래밍으로 소스 코드를 작성할 때 1을 빼는 연산을 제외하고는 해당 수로 나누어떨어질 때에 한해서만 점화식을 적용할 수 있음
- 두 수 중에서 단순히 더 작은 수를 구하고자 할 때는 `min()` 함수를 이용