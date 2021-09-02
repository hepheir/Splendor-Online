# Splendor

온라인 상에서 플레이 가능한 스플렌더 게임을 구현합니다.

## 애자일 개발 프로세스 - 폭포수 모델

본 프로젝트는 계획없이 진행되는 것을 방지하지만, 동시에 지나치게 계획적인 것도 지양하기 위해 애자일 개발 방법론 중 하나인, 폭포수 모델을 사용할 것입니다.

![폭포수 모델도](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Waterfall_model.svg/350px-Waterfall_model.svg.png)

### 요구사항

유명 보드게임 [스플렌더](https://ko.wikipedia.org/wiki/%EC%8A%A4%ED%94%8C%EB%A0%8C%EB%8D%94)를 온라인상에서 지인들과 함께 즐기고 싶어 구현을 시작하였습니다.

### 디자인

본래 스플렌더 보드게임은 이미 존재하는 게임이므로, 당장은 해당 작품의 모든 시스템적, 미적 디자인을 그대로 구현하는데 충실할 것 입니다.

추후, 이미 존재하는 확장팩, 혹은 사용자 커스텀 카드 구성을 지원할 의향이 있습니다.

### 구현

구현은 중요도에 따라 몇 가지 단계로 나누어 순서대로 이루어 질 것입니다.


#### 구현 1단계: \(client\) 스플렌더 게임 컴포넌트 구현

가장 먼저 구현하고자 하는 것은, 스플렌더 게임을 하기위한 모든 컴포넌트입니다.
컴포넌트란, 보드게임을 구성하는 모든 구성품을 일컫는 말로, 게임판, 토큰, 카드 등을 통칭하는 말입니다.

이 단계에서는 보석 토큰, 보석 카드, 귀족 타일 등과 같은 핵심 컴포넌트들의 구현을 1순위로 하고 있습니다.

#### 구현 2단계: \(client\) 스플렌더 게임 GUI 구현

그 다음 순위는 게임 진행을 위한 UI로, 다른 플레이어의 보드 미니어쳐, 게임 진행 로그, 메뉴 등과 같은 것을 구현합니다.

이 단계에서는 1단계에서 구현한 컴포넌트들을 담기위한 가상의 박스나, 그룹을 주로 구현하게 될 것입니다.

#### 구현 3단계: \(server\) 스플렌더 게임 시스템 구현

클라이언트에서 사용하기 위한 GUI의 구현이 충분히 이루어 진 뒤에는 백엔드 서버의 구현을 시작하게 됩니다. 백엔드 서버는 전반적인 게임 로직을 관리하며, 플레이어간의 중재 및 턴 진행을 맡게될 것입니다.

#### 구현 4단계: \(server/client\) 스플렌더 클라이언트와 서버 연동

게임 로직 및 시스템의 설계가 갖추어지면, 그 동안 만들어 둔 시스템과 GUI의 연계를 위한 작업에 들어갑니다.

이 단계가 완료되면 최소한의 게임 플레이가 가능해지도록 하는 것이 목표입니다.

### 검증

어느 정도 개발이 완료되면, 온라인 환경에서 실제 게임플레이를 통해 베타 테스팅을 진행 할 것입니다.

### 유지 보수

위 작업이 모두 끝난 경우, 배포와 함께 유지 보수 단계에 들어갑니다.

본 단계에서는 사용자 경험 향상에 집중할 것입니다. 퍼포먼스 향상 및 카드 애니메이션과 이펙트, 사운드 추가, 그리고 실시간 채팅이나 UNDO와 같은 기능의 구현은 이 단계에서 이루어 질 것입니다.

## Milestone

9월 둘 째주까지는 모든 구현 단계를 완료하는 것이 목표입니다.
