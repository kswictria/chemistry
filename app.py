
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="MOLECULAR PUMP LAB",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .block-container {
        padding: 1rem 2rem !important;
        max-width: 1600px !important;
    }
    header[data-testid="stHeader"] {
        background: transparent;
    }
    #MainMenu, footer {
        visibility: hidden;
    }
    iframe {
        border-radius: 16px;
    }
</style>
""", unsafe_allow_html=True)

HTML = r"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<script type="importmap">
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js",
    "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/"
  }
}
</script>

<style>
* { box-sizing: border-box; }
body {
  margin: 0;
  background: #09111f;
  color: #e8f0fa;
  font-family: Arial, "Malgun Gothic", sans-serif;
}
button, input { font: inherit; }
.header {
  padding: 22px 26px;
  border-bottom: 1px solid #27384b;
  background: #101c2d;
}
.eyebrow {
  color: #55d9c4;
  font-size: 11px;
  letter-spacing: 3px;
  font-weight: bold;
}
h1 {
  margin: 7px 0;
  font-size: 26px;
  letter-spacing: .5px;
}
.subtitle { color: #94a9be; font-size: 13px; }
.layout {
  display: grid;
  grid-template-columns: 265px minmax(0,1fr) 275px;
  gap: 12px;
  padding: 12px;
}
.panel {
  background: #111e30;
  border: 1px solid #283b50;
  border-radius: 12px;
  overflow: hidden;
}
.panel-title {
  font-size: 12px;
  font-weight: bold;
  color: #65dfce;
  letter-spacing: 1px;
  padding: 17px 17px 12px;
  border-bottom: 1px solid #27394d;
}
.controls { padding: 18px; }
.control { margin-bottom: 23px; }
.control-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  font-size: 12px;
}
.value { color: #70e5d1; font-weight: bold; }
.control small {
  display: block;
  color: #8296ad;
  font-size: 11px;
  line-height: 1.5;
  margin-top: 6px;
}
input[type=range] {
  width: 100%;
  accent-color: #39d3b4;
  cursor: pointer;
}
.stage { position: relative; }
#view {
  position: relative;
  height: 475px;
  overflow: hidden;
  background: radial-gradient(circle at center,#1b3450,#070d17);
}
#view canvas { display: block; }
.stage-label {
  position: absolute;
  top: 14px;
  padding: 8px 12px;
  border-radius: 7px;
  background: #091521d9;
  border: 1px solid #344d64;
  font-size: 11px;
  color: #c0d3e5;
  pointer-events: none;
}
.left-label { left: 14px; }
.right-label { right: 14px; }
.legend {
  position: absolute;
  bottom: 14px;
  left: 14px;
  padding: 10px;
  background: #091521dd;
  border: 1px solid #344d64;
  border-radius: 8px;
  font-size: 11px;
  line-height: 1.9;
  pointer-events: none;
}
.dot {
  display: inline-block;
  width: 9px;
  height: 9px;
  border-radius: 100%;
  margin-right: 6px;
}
.info {
  color: #829bb2;
  font-size: 11px;
  padding: 12px 16px;
  line-height: 1.6;
}
.actions {
  display: flex;
  gap: 7px;
  padding: 13px;
  border-top: 1px solid #27394d;
}
button {
  background: #213750;
  color: white;
  border: 1px solid #39536e;
  border-radius: 7px;
  padding: 10px;
  cursor: pointer;
  font-size: 12px;
}
button:hover { background: #305273; }
.primary { background: #087e78; border-color: #20ada0; }
.primary:hover { background: #119f93; }
.actions button { flex: 1; }
.stats { padding: 14px; display: grid; gap: 10px; }
.stat {
  background: #18283c;
  border: 1px solid #2a4057;
  padding: 14px;
  border-radius: 9px;
}
.stat-label {
  color: #9ab0c5;
  font-size: 11px;
  margin-bottom: 7px;
}
.stat-value {
  font-size: 23px;
  font-weight: bold;
  color: #f2f8ff;
}
.stat-unit { font-size: 11px; color: #7e9aaf; }
.graphs {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  padding: 0 12px 12px;
}
.graph {
  padding: 12px;
  background: #111e30;
  border: 1px solid #283b50;
  border-radius: 12px;
}
.graph-title {
  font-size: 12px;
  font-weight: bold;
  margin-bottom: 10px;
}
.graph canvas { width: 100%; height: 170px; }
.theory {
  margin: 0 12px 14px;
  padding: 18px 20px;
  background: #111e30;
  border: 1px solid #283b50;
  border-radius: 12px;
}
.theory h3 { margin-top: 0; font-size: 15px; }
.theory p, .theory li {
  font-size: 12px;
  line-height: 1.8;
  color: #b4c5d7;
}
.formula {
  background: #091521;
  border-left: 3px solid #39d3b4;
  padding: 12px;
  border-radius: 4px;
  font: 12px Consolas, monospace;
  color: #aaf0e4;
  overflow-x: auto;
}
.warning { color: #e7c68a !important; }
@media(max-width: 1050px) {
  .layout { grid-template-columns: 1fr; }
  .graphs { grid-template-columns: 1fr; }
  #view { height: 410px; }
}
</style>
</head>

<body>

<div class="header">
  <div class="eyebrow">MARS LIFE SUPPORT / CHEMISTRY SIMULATION</div>
  <h1>MOLECULAR PUMP LAB</h1>
  <div class="subtitle">
    분자 간 상호작용과 화학 에너지에 따른 선택적 이온 수송
    · 3D 분자기계 시뮬레이션
  </div>
</div>

<div class="layout">

  <div class="panel">
    <div class="panel-title">01 / EXPERIMENT CONTROLS</div>
    <div class="controls">

      <div class="control">
        <div class="control-head">
          <span>온도 T</span>
          <span class="value" id="tv">298 K</span>
        </div>
        <input id="temp" type="range" min="278" max="338"
               step="2" value="298">
        <small>활성화 에너지에 따른 전이속도 변화를 계산</small>
      </div>

      <div class="control">
        <div class="control-head">
          <span>결합 세기 지표 B</span>
          <span class="value" id="bv">1.0</span>
        </div>
        <input id="binding" type="range" min="-1" max="3"
               step="0.1" value="1">
        <small>포획·해리 속도를 조절하는 무차원 매개변수</small>
      </div>

      <div class="control">
        <div class="control-head">
          <span>화학적 구동력 Δμ</span>
          <span class="value" id="ev">6 kJ/mol</span>
        </div>
        <input id="energy" type="range" min="0" max="12"
               step="0.5" value="6">
        <small>펌프의 방향성 전이를 유도하는 자유에너지</small>
      </div>

      <div class="control">
        <div class="control-head">
          <span>초기 원수 농도</span>
          <span class="value" id="cv">3.0 mM</span>
        </div>
        <input id="concentration" type="range"
               min="0.5" max="6" step="0.5" value="3">
        <small>왼쪽 원수 저장조의 목표 이온 농도</small>
      </div>

      <div class="control">
        <div class="control-head">
          <span>초기 농축수 / 원수 농도비</span>
          <span class="value" id="rv">0.5</span>
        </div>
        <input id="ratio" type="range"
               min="0.1" max="3" step="0.1" value="0.5">
        <small>1보다 크면 농도 기울기에 역행하는 수송을 관찰 가능</small>
      </div>

      <div class="control">
        <div class="control-head">
          <span>분자 펌프 개수</span>
          <span class="value" id="nv">12</span>
        </div>
        <input id="pumps" type="range"
               min="1" max="36" step="1" value="12">
        <small>막에 존재하는 펌프의 총 개수</small>
      </div>

      <button id="reset" style="width:100%">
        실험 조건으로 초기화
      </button>
    </div>
  </div>

  <div class="panel stage">
    <div class="panel-title">02 / 3D MOLECULAR ENVIRONMENT</div>

    <div id="view">
      <div class="stage-label left-label">
        원수 / 정화 대상
        <div id="leftCon">3.00 mM</div>
      </div>
      <div class="stage-label right-label">
        농축수 / 이온 회수
        <div id="rightCon">1.50 mM</div>
      </div>

      <div class="legend">
        <div><span class="dot" style="background:#49c8ff"></span>목표 이온</div>
        <div><span class="dot" style="background:#cb8cff"></span>분자 펌프 고리</div>
        <div><span class="dot" style="background:#ffb35c"></span>결합 자리</div>
        <div><span class="dot" style="background:#55dfb0"></span>막 구조</div>
      </div>
    </div>

    <div class="info">
      마우스 드래그: 회전 · 휠: 확대/축소 ·
      이온 입자는 농도를 나타내는 시각적 표본입니다.
      분자 고리의 위치는 반응 상태에 따라 변화합니다.
    </div>

    <div class="actions">
      <button class="primary" id="play">일시정지</button>
      <button id="speed">속도 ×1</button>
      <button id="export">CSV 저장</button>
    </div>
  </div>

  <div class="panel">
    <div class="panel-title">03 / LIVE CHEMICAL ANALYSIS</div>

    <div class="stats">
      <div class="stat">
        <div class="stat-label">시뮬레이션 시간</div>
        <div class="stat-value"><span id="time">0.0</span>
          <span class="stat-unit">s</span></div>
      </div>

      <div class="stat">
        <div class="stat-label">원수의 이온 제거율</div>
        <div class="stat-value"><span id="removed">0.0</span>
          <span class="stat-unit">%</span></div>
      </div>

      <div class="stat">
        <div class="stat-label">막을 통한 순간 순수송량</div>
        <div class="stat-value"><span id="flux">0.000</span>
          <span class="stat-unit">mM/s</span></div>
      </div>

      <div class="stat">
        <div class="stat-label">누적 화학적 일의 추정값</div>
        <div class="stat-value"><span id="work">0.000</span>
          <span class="stat-unit">mJ</span></div>
      </div>

      <div class="stat">
        <div class="stat-label">분자 펌프의 평균 점유율</div>
        <div class="stat-value"><span id="occupancy">0.0</span>
          <span class="stat-unit">%</span></div>
      </div>

      <div class="stat">
        <div class="stat-label">전이 단계의 정방향 / 역방향 속도비</div>
        <div class="stat-value"><span id="kratio">1.00</span>
          <span class="stat-unit">배</span></div>
      </div>
    </div>
  </div>
</div>

<div class="graphs">
  <div class="graph">
    <div class="graph-title">시간에 따른 양쪽 용액의 농도</div>
    <canvas id="chart1"></canvas>
    <div class="info" style="padding:4px">
      <span style="color:#49c8ff">●</span> 원수
      &nbsp;&nbsp;
      <span style="color:#faaf69">●</span> 농축수
      &nbsp; | &nbsp; 단위: mM
    </div>
  </div>

  <div class="graph">
    <div class="graph-title">순수송량과 누적 에너지 지표</div>
    <canvas id="chart2"></canvas>
    <div class="info" style="padding:4px">
      <span style="color:#57e4b9">●</span> 순수송량(mM/s)
      &nbsp;&nbsp;
      <span style="color:#cb8cff">●</span> 누적 일(mJ)
    </div>
  </div>
</div>

<div class="theory">
  <h3>04 / CHEMICAL PRINCIPLES & MODEL</h3>

  <p>
    본 프로그램은 분자기계의 포획·수송·방출·초기화를
    4개 상태로 단순화한 반응속도 모델입니다.
    화학적 자유에너지 공급이 정방향과 역방향 전이속도에
    차이를 만들고, 그 결과 선택적 물질 이동이 발생합니다.
  </p>

  <div class="formula">
    k(T) = k(298) × exp[-Ea/R × (1/T - 1/298)]<br>
    k_forward / k_backward = exp[Δμ/(RT)]<br>
    dP_i/dt = Σ(k_ji P_j - k_ij P_i)<br>
    J = (방출속도 - 역포획속도) × 변환계수<br>
    제거율(%) = (C_initial - C_left)/C_initial × 100
  </div>

  <p>
    <b>교과 연계:</b>
    용액의 농도, 분자 간 상호작용, 활성화 에너지,
    아레니우스 관계, 화학 변화의 에너지 출입.
    확률적 상태 전이와 비평형 구동력은 심화 모델입니다.
  </p>

  <p class="warning">
    ※ 과학적 한계: 실제 이온 선택성, 수화 자유에너지,
    막 투과성, 전기적 중성, 다른 이온과의 경쟁, 실제 펌프의
    분자 구조는 포함하지 않습니다. 반응속도 상수와
    에너지 장벽은 교육용 가정값입니다. 그래프는 실제
    우주 물 재활용 장치의 실험 데이터가 아닙니다.
    누적 일은 1 L 기준으로 환산한 화학적 일의
    단순 추정값이며 실제 장치 소비 전력이 아닙니다.
  </p>
</div>

<script type="module">
import * as THREE from "three";
import { OrbitControls }
  from "three/addons/controls/OrbitControls.js";

// =============================================
// 1. 실험 설정
// =============================================

const $ = id => document.getElementById(id);
const R = 8.314;
const REF_T = 298;
const SCALE = 0.012; // 1 L 저장조 기준 농도 환산 계수
const DT = 0.015;

let running = true;
let speed = 1;
let elapsed = 0;
let chemicalWork = 0;
let currentFlux = 0;

let state = [1, 0, 0, 0];
let left = 3;
let right = 1.5;
let initialLeft = 3;

let history = [];

function param() {
  return {
    T: +$("temp").value,
    B: +$("binding").value,
    E: +$("energy").value,
    C: +$("concentration").value,
    ratio: +$("ratio").value,
    N: +$("pumps").value
  };
}

function updateLabels() {
  const p = param();

  $("tv").textContent = p.T + " K";
  $("bv").textContent = p.B.toFixed(1);
  $("ev").textContent = p.E.toFixed(1) + " kJ/mol";
  $("cv").textContent = p.C.toFixed(1) + " mM";
  $("rv").textContent = p.ratio.toFixed(1);
  $("nv").textContent = p.N;
}

function reset() {
  const p = param();

  elapsed = 0;
  chemicalWork = 0;
  currentFlux = 0;
  left = p.C;
  right = p.C * p.ratio;
  initialLeft = left;

  state = [1, 0, 0, 0];
  history = [];

  updateLabels();
  updateReadings();
  saveHistory();
  syncIons();
  drawCharts();
}

// =============================================
// 2. 화학 반응속도 모델
//
// 4개 상태
// 0: 비어 있음, 왼쪽 방향
// 1: 왼쪽에서 이온 포획
// 2: 이온을 오른쪽으로 이동
// 3: 오른쪽 방출 후 빈 상태
//
// 순환 경로: 0 -> 1 -> 2 -> 3 -> 0
// 모든 과정에는 역반응이 존재한다.
//
// 모델은 화학적 구동력이 1 <-> 2 전이에
// 작용한다고 가정한다.
// =============================================

function getRates() {
  const p = param();

  // 온도에 따른 속도 상수 보정
  const Ea = 18000; // J/mol, 교육용 가정값

  const thermal = Math.exp(
    -Ea / R * (1 / p.T - 1 / REF_T)
  );

  // 결합 세기가 클수록 포획은 유리하지만
  // 해리는 느려지는 모델
  const kon = 0.15 * Math.exp(0.55 * p.B) * thermal;
  const koff = 0.50 * Math.exp(-0.55 * p.B) * thermal;

  // 이동속도는 강한 결합에서 다소 감소한다고 가정
  const ktrans = 0.65 *
    Math.exp(-0.08 * p.B * p.B) * thermal;

  const kreset = 0.8 * thermal;

  // Δμ를 정·역방향 장벽에 대칭적으로 배분
  const driving = p.E * 1000 / (2 * R * p.T);

  const forward = [
    kon * left,
    ktrans * Math.exp(driving),
    koff,
    kreset
  ];

  const backward = [
    koff,
    ktrans * Math.exp(-driving),
    kon * right,
    kreset
  ];

  return {forward, backward, kon, koff};
}

// =============================================
// 3. 상태 확률 미분방정식의 수치 적분
// =============================================

function chemistryStep(dt) {
  const p = param();
  const rates = getRates();

  // 각 순환 단계에서의 정/역방향 흐름
  const f = [];
  const b = [];

  for (let i = 0; i < 4; i++) {
    f[i] = state[i] * rates.forward[i];
    b[i] = state[(i + 1) % 4] * rates.backward[i];
  }

  // Euler 적분의 안정성을 위해
  // 상태별 총 유출이 존재 확률을 초과하지 않게 제한
  for (let i = 0; i < 4; i++) {
    const prev = (i + 3) % 4;
    const out = f[i] + b[prev];

    if (out * dt > state[i] && out > 0) {
      const factor = state[i] / (out * dt);
      f[i] *= factor;
      b[prev] *= factor;
    }
  }

  // 저장조에 없는 이온을 포획할 수 없게 제한
  const leftUse = f[0] * p.N * SCALE * dt;
  if (leftUse > left && leftUse > 0) {
    f[0] *= left / leftUse;
  }

  const rightUse = b[2] * p.N * SCALE * dt;
  if (rightUse > right && rightUse > 0) {
    b[2] *= right / rightUse;
  }

  const changes = [0, 0, 0, 0];

  for (let i = 0; i < 4; i++) {
    const j = (i + 1) % 4;
    const net = (f[i] - b[i]) * dt;

    changes[i] -= net;
    changes[j] += net;
  }

  for (let i = 0; i < 4; i++) {
    state[i] = Math.max(0, state[i] + changes[i]);
  }

  // 수치 오차에 따른 확률 정규화
  const sum = state.reduce((a, b) => a + b, 0);
  for (let i = 0; i < 4; i++) state[i] /= sum;

  // 왼쪽 포획 시 원수 농도 감소
  left -= (f[0] - b[0]) * p.N * SCALE * dt;

  // 오른쪽 방출 시 농축수 농도 증가
  right += (f[2] - b[2]) * p.N * SCALE * dt;

  left = Math.max(0, left);
  right = Math.max(0, right);

  // 오른쪽으로 실제 방출되는 순간 순수송량
  currentFlux = (f[2] - b[2]) * p.N * SCALE;

  // 화학적 일의 단순 추정
  // 1 L 기준: mM × kJ/mol = mJ
  // 구동 전이의 순방향/역방향 차이 사용
  chemicalWork += (
    (f[1] - b[1]) * p.N * SCALE * dt * p.E
  );

  elapsed += dt;
}

// =============================================
// 4. Three.js 3D 환경
// =============================================

const container = $("view");
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x091322);

const camera = new THREE.PerspectiveCamera(
  48, 1, 0.1, 100
);
camera.position.set(9, 6, 11);

const renderer = new THREE.WebGLRenderer({
  antialias: true,
  alpha: false
});

renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setSize(
  container.clientWidth,
  container.clientHeight
);
renderer.outputColorSpace = THREE.SRGBColorSpace;
container.prepend(renderer.domElement);

const controls = new OrbitControls(
  camera, renderer.domElement
);
controls.enableDamping = true;
controls.dampingFactor = 0.06;
controls.minDistance = 5;
controls.maxDistance = 23;

scene.add(new THREE.AmbientLight(0xffffff, 1.15));

const light = new THREE.DirectionalLight(0xffffff, 2);
light.position.set(5, 8, 10);
scene.add(light);

const light2 = new THREE.PointLight(0x2fe6c2, 35);
light2.position.set(-3, 2, 3);
scene.add(light2);

function mat(color, opacity=1) {
  return new THREE.MeshPhongMaterial({
    color,
    transparent: opacity < 1,
    opacity,
    shininess: 75,
    depthWrite: opacity === 1
  });
}

const sphereGeo = new THREE.SphereGeometry(0.12, 12, 12);

function sphere(color, radius, x, y, z) {
  const obj = new THREE.Mesh(
    sphereGeo,
    mat(color)
  );
  obj.scale.setScalar(radius / 0.12);
  obj.position.set(x, y, z);
  scene.add(obj);
  return obj;
}

// 수조 경계
function tank(x) {
  const box = new THREE.BoxGeometry(4.3, 5.7, 6.7);
  const edges = new THREE.EdgesGeometry(box);

  const lines = new THREE.LineSegments(
    edges,
    new THREE.LineBasicMaterial({
      color: 0x45647c,
      transparent: true,
      opacity: 0.45
    })
  );

  lines.position.x = x;
  scene.add(lines);
}

tank(-2.2);
tank(2.2);

// 반투명 분리막
const membrane = new THREE.Mesh(
  new THREE.BoxGeometry(0.14, 5.6, 6.6),
  mat(0x20bca2, 0.14)
);
scene.add(membrane);

// 막 격자
const grid = new THREE.GridHelper(
  6.4, 12, 0x54c6ab, 0x254c57
);
grid.rotation.z = Math.PI / 2;
grid.rotation.x = Math.PI / 2;
grid.material.transparent = true;
grid.material.opacity = 0.22;
scene.add(grid);

// =============================================
// 5. 3D 분자 펌프 모델
// =============================================

const pumpGroup = [];
const pumpPositions = [];

for (let i = 0; i < 36; i++) {
  const col = i % 6;
  const row = Math.floor(i / 6);

  pumpPositions.push({
    y: (row - 2.5) * 0.87,
    z: (col - 2.5) * 1.03
  });
}

function makePump(y, z) {
  const group = new THREE.Group();
  group.position.set(0, y, z);

  // 분자 축
  const axle = new THREE.Mesh(
    new THREE.CylinderGeometry(0.075, 0.075, 1.45, 12),
    mat(0x9eb8d0)
  );
  axle.rotation.z = Math.PI / 2;
  group.add(axle);

  // 결합 자리
  const stationA = new THREE.Mesh(
    new THREE.SphereGeometry(0.16, 14, 14),
    mat(0xffae53)
  );
  stationA.position.x = -0.43;
  group.add(stationA);

  const stationB = new THREE.Mesh(
    new THREE.SphereGeometry(0.16, 14, 14),
    mat(0x55d9b4)
  );
  stationB.position.x = 0.43;
  group.add(stationB);

  // 움직이는 분자 고리
  const ring = new THREE.Mesh(
    new THREE.TorusGeometry(0.25, 0.075, 12, 26),
    mat(0xc88aff)
  );
  ring.rotation.y = Math.PI / 2;
  group.add(ring);

  // 포획된 이온
  const bound = new THREE.Mesh(
    new THREE.SphereGeometry(0.105, 12, 12),
    mat(0x49c8ff)
  );
  group.add(bound);

  scene.add(group);

  return {
    group, ring, bound,
    phase: Math.random() * 6.28,
    visualState: 0
  };
}

for (const pos of pumpPositions) {
  pumpGroup.push(makePump(pos.y, pos.z));
}

// =============================================
// 6. 이온 입자 시각화
// =============================================

const ionLeft = [];
const ionRight = [];

function makeIon(side) {
  const object = sphere(
    side === "L" ? 0x49c8ff : 0xffae72,
    0.095, 0, 0, 0
  );

  object.userData = {
    vx: (Math.random() - 0.5) * 0.025,
    vy: (Math.random() - 0.5) * 0.025,
    vz: (Math.random() - 0.5) * 0.025
  };

  return object;
}

for (let i = 0; i < 100; i++) {
  ionLeft.push(makeIon("L"));
  ionRight.push(makeIon("R"));
}

function randomPlace(object, side) {
  object.position.set(
    (side === "L" ? -1 : 1) *
      (0.35 + Math.random() * 3.6),
    (Math.random() - 0.5) * 5.1,
    (Math.random() - 0.5) * 6.1
  );
}

ionLeft.forEach(o => randomPlace(o, "L"));
ionRight.forEach(o => randomPlace(o, "R"));

function syncIons() {
  // 농도에 비례하도록 시각적 입자 개수 결정
  const countL = Math.min(100, Math.round(left * 17));
  const countR = Math.min(100, Math.round(right * 17));

  ionLeft.forEach((obj, i) => obj.visible = i < countL);
  ionRight.forEach((obj, i) => obj.visible = i < countR);
}

function moveIons(objects, side, T) {
  const motion = Math.sqrt(T / REF_T) * 0.65;

  for (const obj of objects) {
    if (!obj.visible) continue;

    const d = obj.userData;

    d.vx = d.vx * 0.92 +
      (Math.random() - 0.5) * 0.006 * motion;
    d.vy = d.vy * 0.92 +
      (Math.random() - 0.5) * 0.006 * motion;
    d.vz = d.vz * 0.92 +
      (Math.random() - 0.5) * 0.006 * motion;

    obj.position.x += d.vx;
    obj.position.y += d.vy;
    obj.position.z += d.vz;

    const x = obj.position.x;

    if (side === "L" && (x > -0.25 || x < -4.25)) {
      d.vx *= -1;
      obj.position.x = Math.max(-4.2,
        Math.min(-0.3, x));
    }
    if (side === "R" && (x < 0.25 || x > 4.25)) {
      d.vx *= -1;
      obj.position.x = Math.max(0.3,
        Math.min(4.2, x));
    }

    if (Math.abs(obj.position.y) > 2.7) d.vy *= -1;
    if (Math.abs(obj.position.z) > 3.15) d.vz *= -1;
  }
}

// 확률에 따라 각 펌프 상태를 시각화
function sampleState() {
  const r = Math.random();
  let cumulative = 0;

  for (let i = 0; i < 4; i++) {
    cumulative += state[i];
    if (r <= cumulative) return i;
  }
  return 3;
}

function updatePumps(t) {
  const total = param().N;

  pumpGroup.forEach((pump, i) => {
    pump.group.visible = i < total;
    if (i >= total) return;

    if (Math.random() < 0.025) {
      pump.visualState = sampleState();
    }

    const s = pump.visualState;

    const targetX = [-0.65, -0.4, 0.4, 0.65][s];

    pump.ring.position.x +=
      (targetX - pump.ring.position.x) * 0.12;

    pump.ring.rotation.x =
      Math.sin(t * 2 + pump.phase) * 0.16;

    pump.ring.rotation.z =
      Math.cos(t * 1.4 + pump.phase) * 0.12;

    pump.bound.visible = s === 1 || s === 2;
    pump.bound.position.x = pump.ring.position.x;
  });
}

// =============================================
// 7. 지표 및 그래프
// =============================================

function updateReadings() {
  const p = param();

  const removal =
    (initialLeft - left) / Math.max(initialLeft, 0.001) * 100;

  const occupancy = (state[1] + state[2]) * 100;
  const ratio = Math.exp(p.E * 1000 / (R * p.T));

  $("time").textContent = elapsed.toFixed(1);
  $("removed").textContent = removal.toFixed(1);
  $("flux").textContent = currentFlux.toFixed(3);
  $("work").textContent = chemicalWork.toFixed(3);
  $("occupancy").textContent = occupancy.toFixed(1);
  $("kratio").textContent = ratio.toFixed(2);

  $("leftCon").textContent = left.toFixed(2) + " mM";
  $("rightCon").textContent = right.toFixed(2) + " mM";
}

function saveHistory() {
  history.push({
    time: elapsed,
    left: left,
    right: right,
    flux: currentFlux,
    work: chemicalWork,
    occupancy: (state[1] + state[2]) * 100
  });

  if (history.length > 700) {
    history.shift();
  }
}

function prepareCanvas(canvas) {
  const w = canvas.clientWidth;
  const h = canvas.clientHeight;
  const dpr = Math.min(devicePixelRatio, 2);

  canvas.width = Math.round(w * dpr);
  canvas.height = Math.round(h * dpr);

  const ctx = canvas.getContext("2d");
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  return {ctx, w, h};
}

function chart(canvasId, series) {
  const canvas = $(canvasId);
  const {ctx, w, h} = prepareCanvas(canvas);

  const leftPad = 43;
  const rightPad = 13;
  const topPad = 14;
  const bottomPad = 27;

  ctx.clearRect(0, 0, w, h);

  const times = history.map(d => d.time);
  const xmin = times.length ? times[0] : 0;
  const xmax = Math.max(elapsed, xmin + 1);

  const values = series.flatMap(s =>
    history.map(d => s.get(d))
  );

  const ymin = Math.min(0, ...values);
  const ymax = Math.max(0.01, ...values);
  const span = Math.max(0.01, ymax - ymin);

  const xMap = x => leftPad +
    (x - xmin) / (xmax - xmin) *
    (w - leftPad - rightPad);

  const yMap = y => topPad +
    (1 - (y - ymin) / span) *
    (h - topPad - bottomPad);

  ctx.font = "10px Arial";
  ctx.strokeStyle = "#304457";
  ctx.fillStyle = "#8fa8bf";

  for (let i = 0; i <= 4; i++) {
    const y = topPad +
      i * (h - topPad - bottomPad) / 4;

    ctx.beginPath();
    ctx.moveTo(leftPad, y);
    ctx.lineTo(w - rightPad, y);
    ctx.stroke();

    const v = ymax - span * i / 4;
    ctx.fillText(v.toFixed(2), 3, y + 3);
  }

  ctx.fillText(xmin.toFixed(0), leftPad, h - 8);
  ctx.fillText(xmax.toFixed(0) + " s", w - 38, h - 8);

  for (const s of series) {
    ctx.beginPath();
    ctx.strokeStyle = s.color;
    ctx.lineWidth = 2;

    history.forEach((d, i) => {
      const x = xMap(d.time);
      const y = yMap(s.get(d));

      if (i === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    });

    ctx.stroke();
  }
}

function drawCharts() {
  chart("chart1", [
    {color:"#49c8ff", get:d => d.left},
    {color:"#faaf69", get:d => d.right}
  ]);

  chart("chart2", [
    {color:"#57e4b9", get:d => d.flux},
    {color:"#cb8cff", get:d => d.work}
  ]);
}

// =============================================
// 8. 버튼 기능
// =============================================

$("reset").onclick = reset;

$("play").onclick = () => {
  running = !running;
  $("play").textContent = running ? "일시정지" : "재생";
};

$("speed").onclick = () => {
  speed = speed === 1 ? 2 : speed === 2 ? 4 : 1;
  $("speed").textContent = "속도 ×" + speed;
};

$("export").onclick = () => {
  const p = param();

  const header = [
    "time_s", "left_mM", "right_mM",
    "flux_mM_per_s", "work_mJ",
    "occupancy_percent",
    "temperature_K", "binding_B",
    "driving_kJ_per_mol", "pump_count"
  ];

  const rows = history.map(d => [
    d.time, d.left, d.right,
    d.flux, d.work, d.occupancy,
    p.T, p.B, p.E, p.N
  ]);

  const csv = [
    header.join(","),
    ...rows.map(row => row.join(","))
  ].join("\n");

  const blob = new Blob([csv], {
    type:"text/csv;charset=utf-8"
  });

  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");

  a.href = url;
  a.download = "molecular_pump_results.csv";
  document.body.appendChild(a);
  a.click();
  a.remove();

  setTimeout(() => URL.revokeObjectURL(url), 1000);
};

// 농도 초기값을 바꾸는 슬라이더만 초기화
["concentration", "ratio"].forEach(id => {
  $(id).addEventListener("change", reset);
});

// 다른 변인은 실행 중에도 즉시 변경
["temp", "binding", "energy", "pumps"].forEach(id => {
  $(id).addEventListener("input", updateLabels);
});

// =============================================
// 9. 애니메이션 루프
// =============================================

let lastTime = performance.now();
let lastChart = 0;
let lastIonSync = 0;
let lastVisual = 0;

function animate(now) {
  requestAnimationFrame(animate);

  const frameDt = Math.min(
    (now - lastTime) / 1000, 0.05
  );
  lastTime = now;

  if (running) {
    const totalDt = frameDt * speed;
    const steps = Math.max(
      1, Math.ceil(totalDt / DT)
    );
    const stepDt = totalDt / steps;

    for (let i = 0; i < steps; i++) {
      chemistryStep(stepDt);
    }

    lastVisual += frameDt;

    if (lastVisual > 0.04) {
      moveIons(ionLeft, "L", param().T);
      moveIons(ionRight, "R", param().T);
      updatePumps(now / 1000);
      lastVisual = 0;
    }

    if (now - lastIonSync > 350) {
      syncIons();
      lastIonSync = now;
    }

    if (now - lastChart > 400) {
      saveHistory();
      updateReadings();
      drawCharts();
      lastChart = now;
    }
  }

  controls.update();
  renderer.render(scene, camera);
}

// 화면 크기 조절
function resize() {
  const w = container.clientWidth;
  const h = container.clientHeight;

  camera.aspect = w / h;
  camera.updateProjectionMatrix();
  renderer.setSize(w, h);

  drawCharts();
}

window.addEventListener("resize", resize);

reset();
requestAnimationFrame(animate);
</script>

</body>
</html>
"""

components.html(HTML, height=1190, scrolling=True)
