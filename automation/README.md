# cron

- cron job 등록 `crontab -e`

- 기본 문법
```shell
* * * * * <실행할 명령어>
*/5 * * * * /home/ubuntu/damf2/automation/venv/bin/python /home/ubuntu/damf2/automation/0.log/0.log_generate.py   
```
- `python`으로 `0.log_generate.py`를 5분마다 반복
- 분 시 일 월 요일
    - 분: 0-59
    - 시: 0-23
    - 일: 1-31
    - 월: 1-12
    - 요일: 0-6, 0은 일요일

- cron 리스트 확인 `crontab -l`

# melon

- linux chrome 다운로드
- chrome-driver 다운로드

## css 가상 선택자
- [CSS speedrun](https://css-speedrun.netlify.app/)

- `li:nth-of-type(1)` 첫번째 li 선택
- `li:first-child`
```html
<ul>
  <li></li> #
  <li></li>
  <li></li>
</ul>
```

- `p:not(.foo)` foo 클래스 제외
```html
<div>
  <p></p> #
  <p class="foo"></p>
  <p></p> #
  <p></p> #
</div>
```

- `li:nth-of-type(2n+3)` 순서에 함수 사용
```html
<ul>
  <li></li>
  <li></li>
  <li></li> #
  <li></li>
  <li></li> #
  <li></li>
  <li></li> #
</ul>
```

- `div > *` 부모 밑의 자식 전체
```html
<div>
  <span></span> #
  <p> #
    <a></a>
    <span></span>
  </p>
</div>
```

- `span[data-item]` attribute
```html
<div>
  <span data-item="foo"></span> #
  <span></span>
  <div>
    <span></span>
    <span data-item="bar"></span> #
    <span></span>
  </div>
</div>
```

- `p ~ span` 인접
```html
<div>
  <span></span>
  <code></code>
  <span></span>
  <p></p>
  <span></span> #
  <span></span> #
  <p></p>
  <code></code>
  <span></span> #
  <p></p>
</div>
```

- `:enabled` disabled가 없는
```html
<form>
  <input /> #
  <input disabled />
  <input /> #
  <input /> #
  <button disabled></button>
  <button></button> #
</form>
```

- `#one, #two, #five, #six, #nine` id
```html
<ol>
  <li class="me" id="one"></li> #
  <li class="you" id="two"></li> #
  <li class="me" id="three"></li>
  <li class="you" id="four"></li>
  <li class="me" id="five"></li> #
  <li class="you" id="six"></li> #
  <li class="me" id="seven"></li>
  <li class="you" id="eight"></li>
  <li class="me" id="nine"></li> #
  <li class="you" id="ten"></li>
</ol>
```

- `a + span` 인접형제 선택자
```html
<div>
  <span></span>
  <p>
    <a></a>
    <span></span> #
  </p>
  <p>
    <span></span>
    <a></a>
    <span></span> #
    <span></span>
  </p>
  <a></a>
  <span></span> #
</div>
```

- `div#foo > div.foo`
```html
<div id="foo">
  <div class="foo"></div> #
  <div></div>
  <div>
    <div class="foo"></div>
    <div></div>
  </div>
  <div class="foo"></div> #
</div>
```

- `div div span + code:not(.foo)`
```html
<div>
  <div>
    <span></span>
    <code></code> #
  </div>
  <div>
    <code></code>
    <span></span>
    <code></code> #
  </div>
  <div>
    <span></span>
    <code class="foo"></code>
  </div>
  <span></span>
  <code></code>
</div>
```
