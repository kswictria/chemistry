
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="ARES | Molecular Pump",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
html, body, .stApp {
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden !important;
    background: #060c16 !important;
}
header[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
#MainMenu, footer {
    display: none !important;
}
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"],
.block-container {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
    width: 100% !important;
}
iframe {
    width: 100% !important;
    height: 100dvh !important;
    min-height: 500px !important;
    border: none !important;
    display: block !important;
}
</style>
""", unsafe_allow_html=True)

HTML = r"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">

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

html, body {
 margin: 0;
 width: 100%;
 height: 100%;
 overflow: hidden;
 background: #060c16;
 color: #edf5ff;
 font-family: "Malgun Gothic", Arial, sans-serif;
}

button, input { font: inherit; }

button {
 cursor: pointer;
 border: 1px solid #36506a;
 background: #172b43;
 color: #edf5ff;
 border-radius: 9px;
 padding: 10px 15px;
 font-size: 12px;
 transition: .2s;
}

button:hover { background: #284760; }

.primary {
 background: #088b83;
 border-color: #35c9b7;
}

.primary:hover { background: #0aa99b; }

#app {
 position: relative;
 width: 100%;
 height: 100dvh;
 min-height: 480px;
 overflow: hidden;
 background: #070e19;
}

#scene {
 position: absolute;
 inset: 0;
 z-index: 0;
}

#scene canvas {
 display: block;
 width: 100%;
 height: 100%;
}

.overlay {
 position: absolute;
 inset: 0;
 z-index: 2;
 pointer-events: none;
}

.overlay button,
.overlay input,
.overlay .panel {
 pointer-events: auto;
}

.hidden { display: none !important; }

/* ===== 공통 상단 ===== */

.topbar {
 position: absolute;
 top: 0;
 left: 0;
 right: 0;
 z-index: 5;
 height: 65px;
 padding: 0 25px;
 display: flex;
 align-items: center;
 justify-content: space-between;
 background: linear-gradient(
  to bottom,
  rgba(5,12,24,.96),
  rgba(5,12,24,.62)
 );
 border-bottom: 1px solid #ffffff16;
 pointer-events: auto;
}

.logo {
 font-size: 13px;
 font-weight: 800;
 letter-spacing: 2px;
}

.logo span { color: #53e0cc; }

.sublogo {
 font-size: 10px;
 color: #849bb4;
 margin-top: 5px;
 letter-spacing: 1px;
}

.top-actions {
 display: flex;
 align-items: center;
 gap: 9px;
}

.top-actions button {
 padding: 8px 12px;
 background: #14263acb;
}

/* ===== 스토리 ===== */

#storyLayer {
 position: absolute;
 inset: 0;
 z-index: 3;
 pointer-events: none;
}

.scene-info {
 position: absolute;
 left: 28px;
 top: 88px;
 font-size: 10px;
 letter-spacing: 2px;
 color: #83afca;
 text-shadow: 0 2px 10px #000;
}

.story-progress {
 position: absolute;
 right: 28px;
 top: 88px;
 font: 11px Consolas, monospace;
 color: #9abbd1;
}

.alert {
 position: absolute;
 top: 20%;
 left: 50%;
 transform: translateX(-50%);
 padding: 12px 20px;
 border: 1px solid #ff706c;
 border-radius: 6px;
 background: #581d28bb;
 color: #ffd6d2;
 font: bold 12px Consolas, monospace;
 letter-spacing: 2px;
 opacity: 0;
 transition: opacity .4s;
}

.alert.visible {
 opacity: 1;
 animation: pulse 1.5s infinite;
}

@keyframes pulse {
 50% { box-shadow: 0 0 22px #e3484b66; }
}

.story-box {
 position: absolute;
 left: max(5%, 30px);
 right: max(5%, 30px);
 bottom: 4%;
 max-width: 1080px;
 margin: auto;
 padding: 22px 26px;
 border: 1px solid #64829a88;
 border-radius: 13px;
 background: #071321e9;
 box-shadow: 0 15px 60px #0009;
 backdrop-filter: blur(14px);
 pointer-events: auto;
}

.speaker {
 color: #65e6d0;
 font-size: 12px;
 font-weight: bold;
 margin-bottom: 12px;
 letter-spacing: .5px;
}

.story-text {
 font-size: clamp(13px,1.5vw,17px);
 line-height: 1.9;
 min-height: 67px;
 white-space: pre-line;
}

.story-actions {
 display: flex;
 align-items: center;
 justify-content: flex-end;
 gap: 9px;
 margin-top: 12px;
}

.story-actions button { min-width: 100px; }

/* ===== 실험실 ===== */

#labLayer {
 position: absolute;
 inset: 0;
 z-index: 3;
 pointer-events: none;
}

.equation {
 position: absolute;
 top: 81px;
 left: 50%;
 transform: translateX(-50%);
 width: min(650px, 60vw);
 padding: 13px 20px;
 border-radius: 11px;
 border: 1px solid #4c7c86;
 background: #081724df;
 text-align: center;
 backdrop-filter: blur(12px);
}

.eq-title {
 font-size: 10px;
 color: #68e7d1;
 letter-spacing: 1.5px;
 margin-bottom: 8px;
}

.eq-main {
 font-size: clamp(15px,2vw,23px);
 font-family: Georgia, serif;
}

.eq-meaning {
 font-size: 11px;
 color: #a6c0d2;
 margin-top: 7px;
 line-height: 1.6;
}

.chamber-label {
 position: absolute;
 top: 44%;
 text-align: center;
 font-size: 12px;
 color: #d2ebf6;
 text-shadow: 0 2px 12px #000;
}

.chamber-label.left { left: 5%; }
.chamber-label.right { right: 29%; }

.chamber-label strong {
 display: block;
 color: #67d9fb;
 font-size: 21px;
 margin-top: 6px;
}

.chamber-label.right strong { color: #ffb778; }

.flow-label {
 position: absolute;
 left: 43%;
 top: 59%;
 transform: translateX(-50%);
 padding: 8px 12px;
 background: #071624b8;
 border-radius: 18px;
 font-size: 11px;
 color: #65e3cd;
}

/* ===== 제어 패널 ===== */

.panel {
 position: absolute;
 right: 18px;
 top: 81px;
 bottom: 90px;
 width: min(300px, 28vw);
 padding: 20px;
 border: 1px solid #36536c;
 border-radius: 14px;
 background: #091727ee;
 backdrop-filter: blur(16px);
 overflow-y: auto;
}

.panel-heading {
 font-size: 12px;
 font-weight: bold;
 letter-spacing: 1px;
 color: #78e8d6;
 margin-bottom: 21px;
}

.control { margin-bottom: 29px; }

.control-top {
 display: flex;
 justify-content: space-between;
 align-items: center;
 gap: 10px;
 font-size: 12px;
}

.control-value {
 color: #70e4d1;
 font-weight: bold;
 font-size: 12px;
 white-space: nowrap;
}

input[type="range"] {
 width: 100%;
 margin: 13px 0 8px;
 accent-color: #52d9c4;
 cursor: pointer;
}

.effect {
 font-size: 11px;
 line-height: 1.7;
 color: #b0c3d6;
 min-height: 36px;
}

.effect b { color: #6ce5cf; }

.control.selected {
 border-left: 2px solid #52d9c4;
 padding-left: 11px;
 margin-left: -13px;
}

.mini-divider {
 height: 1px;
 background: #ffffff18;
 margin: 19px 0;
}

.bottom-actions {
 display: flex;
 gap: 8px;
 flex-wrap: wrap;
}

.bottom-actions button {
 flex: 1;
 padding: 10px 7px;
}

/* ===== 하단 결과 ===== */

.results {
 position: absolute;
 bottom: 17px;
 left: 22px;
 right: 335px;
 display: flex;
 gap: 10px;
 align-items: stretch;
}

.result {
 min-width: 0;
 flex: 1;
 background: #071624dc;
 border: 1px solid #36536b;
 border-radius: 11px;
 padding: 13px 16px;
 backdrop-filter: blur(12px);
}

.result-name {
 font-size: 10px;
 color: #96aec4;
 margin-bottom: 8px;
}

.result-number {
 font-size: clamp(18px,2.3vw,28px);
 font-weight: bold;
 white-space: nowrap;
}

.result-unit {
 color: #95afc2;
 font-size: 11px;
}

#feedback {
 position: absolute;
 bottom: 112px;
 left: 27px;
 max-width: calc(100% - 365px);
 background: #081725c9;
 border-left: 3px solid #4dd8c0;
 border-radius: 5px;
 padding: 11px 14px;
 font-size: 12px;
 line-height: 1.6;
 color: #bdebe3;
}

/* ===== 그래프 팝업 ===== */

#graphPopup {
 position: absolute;
 left: 22px;
 bottom: 108px;
 width: min(460px, calc(100% - 360px));
 height: 230px;
 background: #0a1a2bea;
 border: 1px solid #45647d;
 border-radius: 11px;
 padding: 16px;
 pointer-events: auto;
 backdrop-filter: blur(15px);
}

.graph-header {
 display: flex;
 justify-content: space-between;
 align-items: center;
 font-size: 12px;
 margin-bottom: 12px;
}

#graph { width: 100%; height: 155px; }

.graph-legend {
 font-size: 10px;
 color: #adc5d8;
}

@media(max-width: 820px) {
 .topbar { padding: 0 12px; height: 58px; }
 .sublogo { display: none; }

 .story-box { left: 12px; right: 12px; padding: 16px; }

 .panel {
  top: auto;
  left: 8px;
  right: 8px;
  bottom: 8px;
  width: auto;
  height: 245px;
  padding: 13px;
 }

 .panel-heading { margin-bottom: 10px; }

 .control {
  margin-bottom: 11px;
 }
 .control input { margin: 5px 0 2px; }
 .control .effect { display: none; }

 .equation {
  top: 68px;
  width: calc(100% - 20px);
  padding: 9px;
 }
 .eq-meaning { font-size: 10px; }
 .chamber-label { top: 34%; font-size: 10px; }
 .chamber-label.right { right: 12%; }
 .chamber-label strong { font-size: 15px; }
 .flow-label { display: none; }

 .results {
  bottom: 262px;
  left: 8px;
  right: 8px;
  gap: 5px;
 }
 .result { padding: 8px; }
 .result-name { font-size: 9px; }
 .result-number { font-size: 16px; }
 #feedback { display: none; }
 #graphPopup {
  left: 8px;
  bottom: 270px;
  width: calc(100% - 16px);
  height: 180px;
 }
 #graph { height: 110px; }
}
</style>
</head>

<body>
<div id="app">

 <div id="scene"></div>

 <div class="topbar">
  <div>
   <div class="logo"><span>ARES</span> / MOLECULAR PUMP</div>
   <div class="sublogo">MARS WATER RECOVERY MISSION</div>
  </div>
  <div class="top-actions">
   <button id="homeBtn" class="hidden">처음으로</button>
   <button id="fullBtn">⛶ 전체화면</button>
  </div>
 </div>

 <!-- 3D 우주선 스토리 -->
 <div id="storyLayer">

  <div class="scene-info" id="sceneInfo">
   DEEP SPACE / CRUISE
  </div>

  <div class="story-progress" id="progress">
   01 / 06
  </div>

  <div class="alert" id="alert">
   WATER RECOVERY WARNING
  </div>

  <div class="story-box">
   <div class="speaker" id="speaker"></div>
   <div class="story-text" id="storyText"></div>

   <div class="story-actions">
    <button id="skip">모두 스킵</button>
    <button class="primary" id="next">다음 →</button>
   </div>
  </div>

 </div>

 <!-- 분자펌프 시뮬레이션 -->
 <div id="labLayer" class="hidden">

  <div class="equation">
   <div class="eq-title" id="eqTitle">
    CHEMICAL MODEL
   </div>
   <div class="eq-main" id="eqMain"></div>
   <div class="eq-meaning" id="eqMeaning"></div>
  </div>

  <div class="chamber-label left">
   원수
   <strong id="leftText">3.00</strong>
   mM
  </div>

  <div class="chamber-label right">
   농축수
   <strong id="rightText">1.00</strong>
   mM
  </div>

  <div class="flow-label" id="flowText">
   이온 수송 중
  </div>

  <div class="panel">
   <div class="panel-heading">
    분자 펌프 조작
   </div>

   <div class="control" id="controlB">
    <div class="control-top">
     <span>결합 친화도</span>
     <span class="control-value" id="valueB">1.0</span>
    </div>
    <input type="range" id="binding"
           min="-1" max="3" step="0.1" value="1">
    <div class="effect" id="effectB"></div>
   </div>

   <div class="control" id="controlE">
    <div class="control-top">
     <span>화학 에너지 공급</span>
     <span class="control-value" id="valueE">6.0 kJ/mol</span>
    </div>
    <input type="range" id="energy"
           min="0" max="12" step="0.5" value="6">
    <div class="effect" id="effectE"></div>
   </div>

   <div class="control" id="controlT">
    <div class="control-top">
     <span>온도</span>
     <span class="control-value" id="valueT">298 K</span>
    </div>
    <input type="range" id="temp"
           min="278" max="338" step="2" value="298">
    <div class="effect" id="effectT"></div>
   </div>

   <div class="mini-divider"></div>

   <div class="bottom-actions">
    <button id="reset">초기화</button>
    <button id="pause" class="primary">일시정지</button>
    <button id="graphBtn">그래프</button>
   </div>
  </div>

  <div id="feedback">
   분자 펌프를 조작하면 이온의 포획·이동·방출이 달라져.
  </div>

  <div class="results">
   <div class="result">
    <div class="result-name">이온 제거율</div>
    <div class="result-number">
     <span id="removal">0.0</span><span class="result-unit">%</span>
    </div>
   </div>
   <div class="result">
    <div class="result-name">순수송 속도</div>
    <div class="result-number">
     <span id="flux">0.000</span>
     <span class="result-unit">mM/s</span>
    </div>
   </div>
   <div class="result">
    <div class="result-name">누적 화학 에너지 교환</div>
    <div class="result-number">
     <span id="work">0.00</span>
     <span class="result-unit">mJ</span>
    </div>
   </div>
  </div>

  <div id="graphPopup" class="hidden">
   <div class="graph-header">
    <b>이온 농도 변화</b>
    <button id="closeGraph">닫기</button>
   </div>
   <canvas id="graph"></canvas>
   <div class="graph-legend">
    <span style="color:#53c8ff">●</span> 원수
    &nbsp;&nbsp;
    <span style="color:#ffb371">●</span> 농축수
    &nbsp; (mM)
   </div>
  </div>

 </div>

</div>

<script type="module">

import * as THREE from "three";
import {OrbitControls} from
 "three/addons/controls/OrbitControls.js";

const $ = id => document.getElementById(id);

const R = 8.314;
const REF = 298;
const SCALE = 0.012;

let mode = "story";
let running = true;
let storyIndex = 0;
let elapsed = 0;
let left = 3;
let right = 1;
let work = 0;
let flux = 0;
let states = [1,0,0,0];
let history = [];
let currentFocus = "B";

// ===========================================
// 1. Three.js 기본 환경
// ===========================================

const mount = $("scene");
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x060d18);

const camera = new THREE.PerspectiveCamera(
 48,1,0.1,200
);

camera.position.set(11,6,18);

const renderer = new THREE.WebGLRenderer({
 antialias:true,
 powerPreference:"high-performance"
});

renderer.setPixelRatio(
 Math.min(window.devicePixelRatio,2)
);
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.35;

mount.appendChild(renderer.domElement);

const controls = new OrbitControls(camera,renderer.domElement);
controls.enableDamping = true;
controls.enabled = false;
controls.minDistance = 5;
controls.maxDistance = 22;
controls.enablePan = false;

scene.add(new THREE.AmbientLight(0xffffff,1.6));

const key = new THREE.DirectionalLight(0xc5e7ff,3);
key.position.set(6,9,12);
scene.add(key);

const glowLight = new THREE.PointLight(0x49d8c7,35);
glowLight.position.set(-4,2,5);
scene.add(glowLight);

function material(color,opacity=1,emissive=0x000000){
 return new THREE.MeshPhongMaterial({
  color,
  emissive,
  transparent:opacity<1,
  opacity,
  shininess:85,
  depthWrite:opacity===1
 });
}

function box(w,h,d,color){
 return new THREE.Mesh(
  new THREE.BoxGeometry(w,h,d),
  material(color)
 );
}

function sphere(r,color){
 return new THREE.Mesh(
  new THREE.SphereGeometry(r,20,16),
  material(color)
 );
}

function cylinder(r,length,color){
 return new THREE.Mesh(
  new THREE.CylinderGeometry(r,r,length,20),
  material(color)
 );
}

// ===========================================
// 2. 우주 배경
// ===========================================

const starPositions=[];

for(let i=0;i<1500;i++){
 const theta=Math.random()*Math.PI*2;
 const z=Math.random()*2-1;
 const radius=40+Math.random()*50;
 const s=Math.sqrt(1-z*z);

 starPositions.push(
  radius*s*Math.cos(theta),
  radius*z,
  radius*s*Math.sin(theta)
 );
}

const starGeometry=new THREE.BufferGeometry();
starGeometry.setAttribute(
 "position",
 new THREE.Float32BufferAttribute(starPositions,3)
);

const stars=new THREE.Points(
 starGeometry,
 new THREE.PointsMaterial({
  color:0xe0eeff,
  size:0.15,
  sizeAttenuation:true
 })
);

scene.add(stars);

const mars=sphere(4,0xb65f42);
mars.position.set(-17,-8,-30);
scene.add(mars);

// ===========================================
// 3. 3D 우주선 모델
// ===========================================

const ship=new THREE.Group();
scene.add(ship);

const hull=cylinder(0.72,5.6,0x9cb4c8);
hull.rotation.z=Math.PI/2;
ship.add(hull);

const nose=new THREE.Mesh(
 new THREE.ConeGeometry(0.72,1.7,30),
 material(0xe0eef5)
);
nose.rotation.z=-Math.PI/2;
nose.position.x=3.6;
ship.add(nose);

const frontBand=cylinder(0.76,0.23,0x3e6780);
frontBand.rotation.z=Math.PI/2;
frontBand.position.x=2.4;
ship.add(frontBand);

// 태양광 패널
for(const direction of [-1,1]){
 const panel=box(2.6,0.08,3.3,0x214b80);
 panel.position.set(-.3,0,direction*2.9);
 ship.add(panel);

 const frame=new THREE.LineSegments(
  new THREE.EdgesGeometry(panel.geometry),
  new THREE.LineBasicMaterial({color:0x81b9e0})
 );
 frame.position.copy(panel.position);
 ship.add(frame);

 for(let i=-2;i<=2;i++){
  const line=box(0.025,0.09,3.25,0x608abb);
  line.position.set(-.3+i*.48,.05,direction*2.9);
  ship.add(line);
 }

 const support=box(.12,.12,1.5,0x9db9ce);
 support.position.set(-.3,0,direction*1.2);
 ship.add(support);
}

// 엔진
for(const z of [-.42,.42]){
 const engine=cylinder(.24,.75,0x3e5c73);
 engine.rotation.z=Math.PI/2;
 engine.position.set(-3.05,-.15,z);
 ship.add(engine);

 const flame=new THREE.Mesh(
  new THREE.ConeGeometry(.2,1.2,20),
  new THREE.MeshBasicMaterial({
   color:0x64d6ff,transparent:true,opacity:.65
  })
 );
 flame.rotation.z=Math.PI/2;
 flame.position.set(-3.85,-.15,z);
 ship.add(flame);
}

// 정화 모듈
const waterModule=box(1.1,1.0,1.25,0x208caa);
waterModule.position.set(-1.15,.88,0);
ship.add(waterModule);

const waterGlow=new THREE.Mesh(
 new THREE.BoxGeometry(1.17,1.07,1.32),
 new THREE.MeshBasicMaterial({
  color:0x4ad9ef,
  transparent:true,
  opacity:0.07
 })
);
waterGlow.position.copy(waterModule.position);
ship.add(waterGlow);

// 경고등
const warningLamp=sphere(.19,0xff4a4f);
warningLamp.position.set(-1.15,1.53,0);
ship.add(warningLamp);

const lampMaterial=new THREE.MeshBasicMaterial({
 color:0xff4444
});
warningLamp.material=lampMaterial;

// 안테나
const antenna=cylinder(.035,1.2,0xc4d9e4);
antenna.position.set(1,1,0);
ship.add(antenna);

const dish=new THREE.Mesh(
 new THREE.ConeGeometry(.5,.25,24),
 material(0xd5e5ee)
);
dish.position.set(1,1.65,0);
ship.add(dish);

// 정화 모듈에서 발생한 문제를 나타내는 입자
const problemParticles=[];

for(let i=0;i<22;i++){
 const particle=sphere(.045,0xff6666);
 particle.position.set(
  -1.15+(Math.random()-.5)*.8,
  1+(Math.random()-.5)*.8,
  (Math.random()-.5)*.8
 );
 ship.add(particle);
 problemParticles.push(particle);
}

// ===========================================
// 4. 움직이는 스토리
// ===========================================

const story = [
 {
  speaker:"항해 시스템 / ARES",
  text:"화성 도착까지 173일.\n탐사선은 제한된 물을 회수하며 항해를 이어가고 있었다.",
  info:"DEEP SPACE / CRUISE",
  camera:[12,7,19],
  target:[0,0,0],
  alarm:false
 },
 {
  speaker:"항해 시스템 / 경고",
  text:"경고. 물 재활용 장치의 이온 제거 성능이 저하되었습니다.\n회수된 물의 용존 이온 농도가 기준을 초과했습니다.",
  info:"WATER SYSTEM / WARNING",
  camera:[8,4,11],
  target:[-1,0.6,0],
  alarm:true
 },
 {
  speaker:"탑재 화학 연구원",
  text:"이온은 물 분자와 상호작용하며 용액에 남아 있어.\n따라서 물을 회수한 뒤에도 별도의 이온 제거가 필요하지.",
  info:"WATER RECOVERY / ANALYSIS",
  camera:[5,3,6.5],
  target:[-1.15,.85,0],
  alarm:true
 },
 {
  speaker:"탑재 화학 연구원",
  text:"기존 분리 장치는 압력이나 소모품 관리가 필요해.\n우리는 새로운 보조 정화 방법을 시험하려고 해.",
  info:"ENGINEERING / ALTERNATIVE",
  camera:[5,2.3,5.5],
  target:[-1.15,.9,0],
  alarm:false
 },
 {
  speaker:"항해 시스템 / 분자 펌프 제안",
  text:"특정 이온을 붙잡고, 화학 에너지를 이용해 이동시킨 뒤 방출하는 분자 펌프.\n이 원리를 물 재활용 장치에 적용할 수 있을까?",
  info:"MOLECULAR PUMP / PROPOSAL",
  camera:[5,4,8],
  target:[-1.15,.8,0],
  alarm:false
 },
 {
  speaker:"탑재 화학 연구원",
  text:"결합 세기, 에너지, 온도를 직접 바꿔 보자.\n분자 펌프가 이온을 얼마나 잘 옮기는지 확인하는 거야.",
  info:"EXPERIMENT / READY",
  camera:[9,5,12],
  target:[0,0,0],
  alarm:false
 }
];

let cameraGoal=new THREE.Vector3(12,7,19);
let targetGoal=new THREE.Vector3();

function showStory(){
 const s=story[storyIndex];

 $("speaker").textContent=s.speaker;
 $("storyText").textContent=s.text;
 $("sceneInfo").textContent=s.info;
 $("progress").textContent=
  String(storyIndex+1).padStart(2,"0")+" / 06";

 $("next").textContent=
  storyIndex===story.length-1 ?
  "시뮬레이션 시작 →" : "다음 →";

 $("alert").classList.toggle("visible",s.alarm);

 cameraGoal.set(...s.camera);
 targetGoal.set(...s.target);

 warningLamp.visible=s.alarm;
 problemParticles.forEach(p=>p.visible=s.alarm);
}

$("next").onclick=()=>{
 if(storyIndex<story.length-1){
  storyIndex++;
  showStory();
 } else {
  enterLab();
 }
};

$("skip").onclick=enterLab;

// ===========================================
// 5. 3D 실험실 구성
// ===========================================

const lab=new THREE.Group();
lab.visible=false;
scene.add(lab);

const membrane=new THREE.Mesh(
 new THREE.BoxGeometry(.16,5.4,6.2),
 material(0x48ceb4,.22)
);
lab.add(membrane);

// 막의 테두리
const membraneEdges=new THREE.LineSegments(
 new THREE.EdgesGeometry(
  new THREE.BoxGeometry(.2,5.4,6.2)
 ),
 new THREE.LineBasicMaterial({color:0x57d9c1})
);
lab.add(membraneEdges);

// 수조 경계
for(const x of [-2.2,2.2]){
 const boundary=new THREE.LineSegments(
  new THREE.EdgesGeometry(
   new THREE.BoxGeometry(4.3,5.5,6.4)
  ),
  new THREE.LineBasicMaterial({
   color:0x53718b,
   transparent:true,
   opacity:.50
  })
 );
 boundary.position.x=x;
 lab.add(boundary);
}

const pumps=[];

// 분자 펌프 12개
for(let i=0;i<12;i++){
 const group=new THREE.Group();
 const row=Math.floor(i/4);
 const col=i%4;

 group.position.set(
  0,(row-1)*1.45,(col-1.5)*1.45
 );

 const axle=cylinder(.07,1.5,0xb7cbd9);
 axle.rotation.z=Math.PI/2;
 group.add(axle);

 const leftSite=sphere(.15,0xf5aa54);
 leftSite.position.x=-.45;
 group.add(leftSite);

 const rightSite=sphere(.15,0x49ddb8);
 rightSite.position.x=.45;
 group.add(rightSite);

 const ring=new THREE.Mesh(
  new THREE.TorusGeometry(.25,.075,12,30),
  material(0xc18af5)
 );
 ring.rotation.y=Math.PI/2;
 group.add(ring);

 const cargo=sphere(.12,0x45c9ff);
 group.add(cargo);

 lab.add(group);

 pumps.push({
  group,ring,cargo,
  state:0,
  phase:Math.random()*6.28,
  pulse:0
 });
}

// 이온 입자들
const leftParticles=[];
const rightParticles=[];

function addIon(side){
 const obj=sphere(.085,
  side==="L" ? 0x4bc8ff : 0xffb16e
 );

 obj.position.set(
  (side==="L"?-1:1)*(.3+Math.random()*3.7),
  (Math.random()-.5)*5,
  (Math.random()-.5)*5.8
 );

 obj.userData.velocity=new THREE.Vector3(
  (Math.random()-.5)*.025,
  (Math.random()-.5)*.025,
  (Math.random()-.5)*.025
 );

 lab.add(obj);
 return obj;
}

for(let i=0;i<90;i++){
 leftParticles.push(addIon("L"));
 rightParticles.push(addIon("R"));
}

// ===========================================
// 6. 화학 계산 모델
// ===========================================

// 교육용 4상태 모형
//
// 0: 왼쪽에서 이온을 기다리는 펌프
// 1: 이온 포획
// 2: 오른쪽으로 이동
// 3: 이온 방출 후 초기화
//
// 0 → 1 → 2 → 3 → 0
//
// 모든 과정에는 역반응이 존재한다.
// 화학적 구동력은 1 ↔ 2 전이에 작용한다.
//
// 모델의 계수는 실제 장치의 측정값이 아닌 가정값이다.

function params(){
 return {
  B:+$("binding").value,
  E:+$("energy").value,
  T:+$("temp").value
 };
}

function rates(){
 const p=params();

 const thermal=Math.exp(
  -18000/R*(1/p.T-1/REF)
 );

 const kon=.15*Math.exp(.55*p.B)*thermal;
 const koff=.50*Math.exp(-.55*p.B)*thermal;

 const move=.65*
  Math.exp(-.08*p.B*p.B)*thermal;

 const reset=.8*thermal;
 const drive=p.E*1000/(2*R*p.T);

 return {
  f:[
   kon*left,
   move*Math.exp(drive),
   koff,
   reset
  ],
  b:[
   koff,
   move*Math.exp(-drive),
   kon*right,
   reset
  ],
  kon,koff,thermal
 };
}

function chemistryStep(dt){
 const rt=rates();
 const f=[],b=[];

 for(let i=0;i<4;i++){
  f[i]=states[i]*rt.f[i];
  b[i]=states[(i+1)%4]*rt.b[i];
 }

 // 확률 유출량 제한
 for(let i=0;i<4;i++){
  const previous=(i+3)%4;
  const out=f[i]+b[previous];

  if(out*dt>states[i] && out>0){
   const q=states[i]/(out*dt);
   f[i]*=q;
   b[previous]*=q;
  }
 }

 // 저장조의 음수 농도 방지
 const leftUse=f[0]*12*SCALE*dt;
 if(leftUse>left && leftUse>0){
  f[0]*=left/leftUse;
 }

 const rightUse=b[2]*12*SCALE*dt;
 if(rightUse>right && rightUse>0){
  b[2]*=right/rightUse;
 }

 const d=[0,0,0,0];

 for(let i=0;i<4;i++){
  const j=(i+1)%4;
  const net=(f[i]-b[i])*dt;
  d[i]-=net;
  d[j]+=net;
 }

 for(let i=0;i<4;i++){
  states[i]=Math.max(0,states[i]+d[i]);
 }

 const total=states.reduce((a,b)=>a+b,0);
 states=states.map(x=>x/total);

 left=Math.max(0,
  left-(f[0]-b[0])*12*SCALE*dt
 );

 right=Math.max(0,
  right+(f[2]-b[2])*12*SCALE*dt
 );

 flux=(f[2]-b[2])*12*SCALE;

 // 1 L 기준의 이상적인 화학적 일 교환 추정
 work+=(f[1]-b[1])*12*SCALE*dt*params().E;

 elapsed+=dt;
}

function reset(){
 elapsed=0;
 left=3;
 right=1;
 work=0;
 flux=0;
 states=[1,0,0,0];
 history=[];
 pumps.forEach(p=>{
  p.state=0;
  p.ring.position.x=-.65;
 });
 record();
 updateUI();
 updateParticles();
}

// ===========================================
// 7. 화학식과 조작 결과 연결
// ===========================================

function focusEquation(which){
 currentFocus=which;

 ["B","E","T"].forEach(id=>{
  $("control"+id).classList.toggle(
   "selected",id===which
  );
 });

 updateEquation();
}

function updateEquation(){
 const p=params();
 const rt=rates();

 $("valueB").textContent=p.B.toFixed(1);
 $("valueE").textContent=p.E.toFixed(1)+" kJ/mol";
 $("valueT").textContent=p.T+" K";

 $("effectB").innerHTML=
  `포획 계수 <b>${rt.kon.toFixed(2)}</b> · `+
  `해리 계수 <b>${rt.koff.toFixed(2)}</b>`;

 $("effectE").innerHTML=
  `이동 전이의 정·역방향 속도비 `+
  `<b>${Math.exp(p.E*1000/(R*p.T)).toFixed(1)}배</b>`;

 $("effectT").innerHTML=
  `298 K 대비 반응속도 계수 `+
  `<b>${rt.thermal.toFixed(2)}배</b>`;

 if(currentFocus==="B"){
  $("eqTitle").textContent=
   "결합 친화도 · 포획과 해리";
  $("eqMain").innerHTML=
   "k<sub>on</sub> ∝ e<sup>0.55B</sup> &nbsp;"+
   "k<sub>off</sub> ∝ e<sup>−0.55B</sup>";
  $("eqMeaning").textContent=
   "B 증가 → 이온 포획은 쉬워지고, 방출은 느려지는 모형";
 }
 else if(currentFocus==="E"){
  $("eqTitle").textContent=
   "화학적 구동력 · 분자 이동";
  $("eqMain").innerHTML=
   "k<sub>+</sub>/k<sub>−</sub> = "+
   "exp(Δμ / RT)";
  $("eqMeaning").textContent=
   "에너지 공급 증가 → 막 통과 전이의 정방향 비율 증가";
 }
 else {
  $("eqTitle").textContent=
   "온도 · 활성화 에너지";
  $("eqMain").innerHTML=
   "k(T) = k(298) exp[−E<sub>a</sub>/R"+
   "(1/T − 1/298)]";
  $("eqMeaning").textContent=
   "온도 변화 → 포획·이동·방출의 반응속도 변화";
 }
}

function feedback(){
 const p=params();

 if(currentFocus==="B"){
  $("feedback").textContent=
   p.B>2 ?
   "결합이 강해 이온을 잡기 쉽지만, 놓는 과정이 느려질 수 있어." :
   p.B<0 ?
   "결합이 약해서 이온을 포획하기 어려운 조건이야." :
   "포획과 방출이 경쟁하고 있어. 결합 세기를 바꿔 비교해 봐.";
 }
 else if(currentFocus==="E"){
  $("feedback").textContent=
   p.E===0 ?
   "외부 화학 구동력이 없어. 농도 차에 따른 이동을 관찰해 봐." :
   "화학 에너지가 막 통과 단계의 방향성을 바꾸고 있어.";
 }
 else {
  $("feedback").textContent=
   p.T>315 ?
   "온도가 높아져 전이속도가 증가했어. 전체 정화율도 확인해 봐." :
   p.T<290 ?
   "온도가 낮아 전이속도가 느려졌어." :
   "온도에 따라 활성화 장벽을 넘는 전이속도가 달라져.";
 }
}

$("binding").addEventListener("input",()=>{
 focusEquation("B");
 feedback();
});

$("energy").addEventListener("input",()=>{
 focusEquation("E");
 feedback();
});

$("temp").addEventListener("input",()=>{
 focusEquation("T");
 feedback();
});

// ===========================================
// 8. 3D 움직임
// ===========================================

function updateParticles(){
 const countL=Math.min(90,Math.round(left*22));
 const countR=Math.min(90,Math.round(right*22));

 leftParticles.forEach((p,i)=>p.visible=i<countL);
 rightParticles.forEach((p,i)=>p.visible=i<countR);
}

function moveParticles(arr,side,dt){
 const thermal=Math.sqrt(params().T/REF);
 const scale=Math.min(dt*60,2);

 for(const obj of arr){
  if(!obj.visible)continue;

  const v=obj.userData.velocity;

  v.x=v.x*.97+(Math.random()-.5)*.003*thermal;
  v.y=v.y*.97+(Math.random()-.5)*.003*thermal;
  v.z=v.z*.97+(Math.random()-.5)*.003*thermal;

  obj.position.addScaledVector(v,scale);

  if(side==="L"){
   if(obj.position.x>-.22 || obj.position.x< -4.25){
    v.x*=-1;
    obj.position.x=Math.max(-4.2,
     Math.min(-.25,obj.position.x));
   }
  } else {
   if(obj.position.x<.22 || obj.position.x>4.25){
    v.x*=-1;
    obj.position.x=Math.max(.25,
     Math.min(4.2,obj.position.x));
   }
  }

  if(Math.abs(obj.position.y)>2.55){
   v.y*=-1;
   obj.position.y=THREE.MathUtils.clamp(
    obj.position.y,-2.55,2.55
   );
  }
  if(Math.abs(obj.position.z)>3){
   v.z*=-1;
   obj.position.z=THREE.MathUtils.clamp(
    obj.position.z,-3,3
   );
  }
 }
}

// 개별 펌프의 확률적 상태 변화
function updatePumps(dt,t){
 const rt=rates();

 pumps.forEach(p=>{
  const s=p.state;

  const forwardRate=rt.f[s];
  const prev=(s+3)%4;
  const backwardRate=rt.b[prev];

  const sum=forwardRate+backwardRate;
  const probability=1-Math.exp(-sum*dt);

  if(sum>0 && Math.random()<probability){
   const forward=Math.random()<
    forwardRate/sum;

   p.state=forward ? (s+1)%4 : prev;
   p.pulse=1;
  }

  const target=[-.62,-.43,.43,.62][p.state];

  p.ring.position.x=THREE.MathUtils.lerp(
   p.ring.position.x,target,
   Math.min(1,dt*5)
  );

  p.ring.rotation.x=Math.sin(t*2+p.phase)*.15;
  p.ring.rotation.z=Math.cos(t*1.4+p.phase)*.10;

  p.cargo.visible=p.state===1||p.state===2;
  p.cargo.position.x=p.ring.position.x;

  p.pulse*=Math.exp(-4*dt);
  p.ring.scale.setScalar(1+.12*p.pulse);
 });
}

// ===========================================
// 9. 결과 및 그래프
// ===========================================

function updateUI(){
 const removal=(3-left)/3*100;

 $("removal").textContent=removal.toFixed(1);
 $("flux").textContent=flux.toFixed(3);
 $("work").textContent=work.toFixed(2);

 $("leftText").textContent=left.toFixed(2);
 $("rightText").textContent=right.toFixed(2);

 $("flowText").textContent=
  flux>0.001 ? "이온 이동 →" :
  flux<-.001 ? "← 역방향 이동" :
  "순수송량 거의 0";

 updateEquation();
}

function record(){
 history.push({
  t:elapsed,
  l:left,
  r:right,
  f:flux
 });

 if(history.length>500)history.shift();
}

function drawGraph(){
 if($("graphPopup").classList.contains("hidden"))return;

 const canvas=$("graph");
 const rect=canvas.getBoundingClientRect();
 const w=Math.max(100,rect.width);
 const h=Math.max(90,rect.height);
 const dpr=Math.min(devicePixelRatio,2);

 canvas.width=w*dpr;
 canvas.height=h*dpr;

 const ctx=canvas.getContext("2d");
 ctx.setTransform(dpr,0,0,dpr,0,0);
 ctx.clearRect(0,0,w,h);

 const minT=history[0]?.t??0;
 const maxT=Math.max(elapsed,minT+1);
 const maxY=Math.max(3.2,...history.map(d=>d.r));

 const x=t=>35+(t-minT)/(maxT-minT)*(w-47);
 const y=v=>12+(1-v/maxY)*(h-30);

 ctx.strokeStyle="#3a5268";
 ctx.fillStyle="#93abc0";
 ctx.font="10px Arial";

 for(let i=0;i<4;i++){
  const yy=12+i*(h-30)/3;
  ctx.beginPath();
  ctx.moveTo(35,yy);
  ctx.lineTo(w-12,yy);
  ctx.stroke();
  ctx.fillText((maxY*(1-i/3)).toFixed(1),3,yy+3);
 }

 for(const [key,color] of [
  ["l","#53c8ff"],
  ["r","#ffb371"]
 ]){
  ctx.strokeStyle=color;
  ctx.lineWidth=2;
  ctx.beginPath();

  history.forEach((d,i)=>{
   if(i===0)ctx.moveTo(x(d.t),y(d[key]));
   else ctx.lineTo(x(d.t),y(d[key]));
  });

  ctx.stroke();
 }
}

$("graphBtn").onclick=()=>{
 $("graphPopup").classList.toggle("hidden");
 drawGraph();
};

$("closeGraph").onclick=()=>{
 $("graphPopup").classList.add("hidden");
};

$("reset").onclick=()=>{
 reset();
 feedback();
};

$("pause").onclick=()=>{
 running=!running;
 $("pause").textContent=
  running?"일시정지":"재생";
};

// ===========================================
// 10. 장면 전환 및 전체화면
// ===========================================

function enterLab(){
 mode="lab";
 ship.visible=false;
 lab.visible=true;
 stars.visible=false;
 mars.visible=false;

 $("storyLayer").classList.add("hidden");
 $("labLayer").classList.remove("hidden");
 $("homeBtn").classList.remove("hidden");

 camera.position.set(9,6,12);
 controls.target.set(0,0,0);
 controls.enabled=true;
 controls.update();

 reset();
 focusEquation("B");
 feedback();
}

$("homeBtn").onclick=()=>{
 mode="story";
 storyIndex=0;

 lab.visible=false;
 ship.visible=true;
 stars.visible=true;
 mars.visible=true;

 controls.enabled=false;

 $("storyLayer").classList.remove("hidden");
 $("labLayer").classList.add("hidden");
 $("homeBtn").classList.add("hidden");

 camera.position.set(12,7,19);
 controls.target.set(0,0,0);

 showStory();
};

$("fullBtn").onclick=async()=>{
 try{
  if(!document.fullscreenElement){
   await document.documentElement.requestFullscreen();
  }else{
   await document.exitFullscreen();
  }
 }catch(e){
  $("fullBtn").textContent="브라우저 전체화면 이용";
  console.warn("Fullscreen unavailable:",e);
 }
};

document.addEventListener("fullscreenchange",()=>{
 $("fullBtn").textContent=
  document.fullscreenElement?
  "전체화면 종료":"⛶ 전체화면";
});

// ===========================================
// 11. 화면 비율
// ===========================================

function resize(){
 const w=Math.max(1,mount.clientWidth);
 const h=Math.max(1,mount.clientHeight);

 camera.aspect=w/h;
 camera.updateProjectionMatrix();
 renderer.setSize(w,h,false);

 drawGraph();
}

new ResizeObserver(resize).observe(mount);
window.addEventListener("resize",resize);

// ===========================================
// 12. 메인 애니메이션
// ===========================================

let last=performance.now();
let graphTimer=0;
let visualTimer=0;

function animate(now){
 requestAnimationFrame(animate);

 const dt=Math.min((now-last)/1000,.045);
 last=now;

 if(mode==="story"){
  const s=story[storyIndex];

  camera.position.lerp(cameraGoal,Math.min(1,dt*1.4));
  controls.target.lerp(targetGoal,Math.min(1,dt*1.4));

  // 우주선이 가만히 떠 있는 대신 계속 항해
  ship.rotation.y=Math.sin(now*.00035)*.14;
  ship.rotation.z=Math.sin(now*.0006)*.035;
  ship.position.y=Math.sin(now*.0005)*.12;

  if(s.alarm){
   warningLamp.visible=true;
   warningLamp.scale.setScalar(
    .8+.35*Math.sin(now*.012)
   );
   waterGlow.material.opacity=
    .08+.15*Math.abs(Math.sin(now*.004));

   problemParticles.forEach((p,i)=>{
    p.position.y+=dt*(.15+i%4*.045);
    if(p.position.y>2.5)p.position.y=.5;
   });
  }else{
   waterGlow.material.opacity=.045;
  }

  // 별 배경의 느린 움직임
  stars.rotation.y+=dt*.0018;

  controls.update();
 }
 else {
  if(running){
   // 계산 결과와 분자 움직임을 동시에 갱신
   const steps=Math.max(1,Math.ceil(dt/.004));
   for(let i=0;i<steps;i++){
    chemistryStep(dt/steps);
   }

   visualTimer+=dt;
   graphTimer+=dt;

   updatePumps(dt,now/1000);

   if(visualTimer>.04){
    moveParticles(leftParticles,"L",visualTimer);
    moveParticles(rightParticles,"R",visualTimer);
    visualTimer=0;
   }

   if(graphTimer>.25){
    record();
    updateUI();
    updateParticles();
    drawGraph();
    graphTimer=0;
   }
  }

  controls.update();
 }

 renderer.render(scene,camera);
}

showStory();
reset();
resize();
requestAnimationFrame(animate);

</script>
</body>
</html>
"""

components.html(HTML, height=1000, scrolling=False)
