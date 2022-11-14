This is a mermaid diagram, you may need to install a [Browser Plugin](https://github.com/BackMarket/github-mermaid-extension) or [VsCode extension](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid) or similar to view it.

You can also [view it full screen as an SVG](https://mermaid.ink/svg/c2VxdWVuY2VEaWFncmFtCiAgc3RhcnQtPj5kaXZpZGlyOiBjYWxscyB4NAogIGRpdmlkaXItLT4+c3RhcnQ6IHJldHVybnMgZmxvYXQKICBzdGFydC0+Pm11bHRpcGxpY2FyOiBjYWxscyB4NAogIG11bHRpcGxpY2FyLS0+PnN0YXJ0OiByZXR1cm5zIGZsb2F0CiAgc3RhcnQtPj5yZXN0YXI6IGNhbGxzIHg0CiAgcmVzdGFyLS0+PnN0YXJ0OiByZXR1cm5zIGZsb2F0CiAgc3RhcnQtPj5zdW1hcjogY2FsbHMgeDQKICBzdW1hci0tPj5zdGFydDogcmV0dXJucyBmbG9hdAo=)        

```mermaid
sequenceDiagram
  start->>dividir: calls x4
  dividir-->>start: returns float
  start->>multiplicar: calls x4
  multiplicar-->>start: returns float
  start->>restar: calls x4
  restar-->>start: returns float
  start->>sumar: calls x4
  sumar-->>start: returns float

```
