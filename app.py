
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="MOLECULAR PUMP | MARS MISSION",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
.block-container {
    padding: 0.5rem 1rem !important;
    max-width: 1700px !important;
}
header[data-testid="stHeader"] {background: transparent;}
#MainMenu, footer {visibility: hidden;}
iframe {border-radius: 14px;}
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
 "imports":{
  "three":"https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js",
  "three/addons/":"https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/"
 }
}
</script>
<style>
*{box-sizing:border-box}
body{margin:0;background:#080f1c;color:#eaf2fc;
font-family:"Malgun Gothic",Arial,sans-serif}
button,input{font:inherit}
button{cursor:pointer;border:1px solid #35536b;
background:#1b3049;color:#eaf5ff;border-radius:8px;
padding:11px 15px;font-size:12px}
button:hover{background:#294966}
.primary{background:#087f78;border-color:#28bcae}
.primary:hover{background:#109c90}
.muted{color:#98adc3}
.hidden{display:none!important}
.top{padding:17px 24px;background:#101d2e;
border-bottom:1px solid #284157}
.kicker{font-size:10px;letter-spacing:2.5px;
font-weight:bold;color:#60e6d0}
h1{font-size:23px;margin:6px 0}
.desc{font-size:12px;color:#9bb1c7;line-height:1.6}
#viewport{position:relative;height:530px;
background:radial-gradient(circle,#19304b,#070d17);
overflow:hidden}
#viewport canvas{display:block}
#introUI{position:absolute;inset:0;pointer-events:none}
.ship-title{position:absolute;top:23px;left:26px;
font-size:12px;letter-spacing:1.5px;color:#95dfe4}
.chapter{position:absolute;top:24px;right:26px;
font-size:11px;color:#a5bad0}
.novel{position:absolute;left:3%;right:3%;bottom:18px;
padding:21px 23px;background:#091423ed;
border:1px solid #4c6b83;border-radius:12px;
box-shadow:0 8px 40px #0009;pointer-events:auto}
.speaker{font-size:12px;font-weight:bold;color:#63e2d1;
margin-bottom:10px}
.story-text{font-size:15px;line-height:1.9;
min-height:85px;white-space:pre-line}
.novel-actions{display:flex;justify-content:flex-end;
gap:9px;margin-top:13px}
#gameUI{position:relative}
.formula-panel{background:#102035;border-bottom:1px solid #314861;
padding:15px 18px}
.formula-title{font-size:11px;color:#61e3d0;
letter-spacing:1.5px;margin-bottom:12px;font-weight:bold}
.formula-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:9px}
.eq{background:#091725;border:1px solid #34485d;
border-radius:9px;padding:12px;transition:.2s}
.eq.active{border-color:#56e0c6;
box-shadow:0 0 0 1px #56e0c655;
background:#10302f}
.eq-name{font-size:11px;font-weight:bold;color:#77dfcd}
.eq-math{font:15px Georgia,serif;color:#f2f6ff;
margin:11px 0}
.eq-explain{font-size:11px;color:#9bb1c5;line-height:1.55}
.eq-value{color:#6fe1d2;font-weight:bold}
.workarea{display:grid;grid-template-columns:260px minmax(0,1fr) 255px;
gap:11px;padding:11px}
.panel{border:1px solid #293e54;background:#111e30;
border-radius:10px;overflow:hidden}
.panel-head{font-size:11px;color:#6ee3d0;letter-spacing:1px;
font-weight:bold;padding:13px 15px;border-bottom:1px solid #294055}
.controls{padding:15px}
.control{margin-bottom:21px}
.control-line{display:flex;justify-content:space-between;
font-size:12px;gap:8px}
.control-line span:last-child{color:#66e1cd;font-weight:bold}
.control input{width:100%;accent-color:#45d5c3;margin:10px 0 3px}
.control small{display:block;font-size:10px;line-height:1.6;
color:#91a6bc}
.stage{position:relative;min-height:390px;
background:radial-gradient(circle,#1c344d,#08111e)}
#labMount{height:390px}
.stage-tag{position:absolute;z-index:2;top:12px;
padding:8px;background:#091521d9;border:1px solid #37516a;
border-radius:6px;font-size:11px;pointer-events:none}
.stage-tag.left{left:12px}
.stage-tag.right{right:12px;text-align:right}
.legend{display:flex;flex-wrap:wrap;gap:14px;
padding:12px;font-size:11px;color:#b8cadb}
.dot{display:inline-block;border-radius:50%;height:9px;
width:9px;margin-right:5px}
.lab-actions{display:flex;gap:8px;padding:12px;
border-top:1px solid #293e54}
.lab-actions button{flex:1}
.stats{padding:12px;display:grid;gap:10px}
.stat{background:#19293e;padding:13px;border-radius:8px;
border:1px solid #2c4056}
.stat-label{font-size:11px;color:#9cb2c9;line-height:1.5}
.stat-number{font-size:21px;font-weight:bold;margin-top:7px}
.stat-unit{font-size:11px;color:#8ca5ba}
.details{padding:0 11px 15px;display:grid;
grid-template-columns:1fr 1fr;gap:11px}
.chart-box{background:#111e30;border:1px solid #293e54;
border-radius:10px;padding:15px}
.chart-heading{font-size:12px;font-weight:bold;margin-bottom:8px}
.chart-box canvas{width:100%;height:170px}
.chart-note{font-size:10px;color:#9ab0c7;margin-top:7px}
.learning{margin:0 11px 15px;background:#111e30;
border:1px solid #293e54;border-radius:10px;padding:18px}
.learning h3{font-size:14px;margin:0 0 12px}
.learning p,.learning li{font-size:12px;color:#adc0d3;line-height:1.9}
.learning b{color:#edf5fd}
.learning .notice{color:#eac891}
.intro-footer{padding:14px 20px;color:#7891a8;font-size:11px}
@media(max-width:1050px){
 .workarea{grid-template-columns:1fr}
 .formula-grid{grid-template-columns:1fr}
 .details{grid-template-columns:1fr}
 #viewport{height:520px}
}
</style>
</head>
<body>

<div class="top">
 <div class="kicker">MARS EXPLORATION / INTERACTIVE CHEMISTRY</div>
 <h1>MOLECULAR PUMP LAB</h1>
 <div class="desc" id="topDescription">
  화성 탐사선의 물 재활용 시스템에 문제가 발생했습니다.
 </div>
</div>

<!-- 시작 화면 -->
<div id="introScreen">
 <div id="viewport">
  <div id="introUI">
   <div class="ship-title">MISSION ARES / WATER RECOVERY SYSTEM</div>
   <div class="chapter" id="chapter">PROLOGUE 01 / 07</div>
   <div class="novel">
    <div class="speaker" id="speaker">항해 시스템</div>
    <div class="story-text" id="storyText"></div>
    <div class="novel-actions">
     <button id="skipStory">모두 스킵</button>
     <button class="primary" id="nextStory">다음 대화 →</button>
    </div>
   </div>
  </div>
 </div>
 <div class="intro-footer">
  3D 우주선 모델 · 마우스 드래그로 시점 변경 ·
  실제 우주선이나 검증된 장비를 재현한 모델은 아닙니다.
 </div>
</div>

<!-- 실험실 -->
<div id="gameUI" class="hidden">

 <div class="formula-panel">
  <div class="formula-title">
   CHEMISTRY EQUATIONS / 슬라이더와 연결된 화학 원리
  </div>
  <div class="formula-grid">

   <div class="eq" id="eq-binding">
    <div class="eq-name">① 분자 간 상호작용 · 포획과 해리</div>
    <div class="eq-math">
      k<sub>on</sub> ∝ e<sup>0.55B</sup>,
      &nbsp;k<sub>off</sub> ∝ e<sup>−0.55B</sup>
    </div>
    <div class="eq-explain">
     B는 결합 친화도를 나타내는 모형 변수야.
     증가하면 이온을 잡기 쉬워지지만 놓기 어려워져.
     <div class="eq-value" id="bindingResult"></div>
    </div>
   </div>

   <div class="eq" id="eq-temp">
    <div class="eq-name">② 활성화 에너지 · 온도와 반응속도</div>
    <div class="eq-math">
     k(T)=k(298) exp[−E<sub>a</sub>/R(1/T−1/298)]
    </div>
    <div class="eq-explain">
     온도가 달라지면 상태 전이 속도도 달라져.
     E<sub>a</sub>는 모형에서 18 kJ/mol로 가정해.
     <div class="eq-value" id="tempResult"></div>
    </div>
   </div>

   <div class="eq" id="eq-energy">
    <div class="eq-name">③ 화학적 자유에너지 · 방향성 수송</div>
    <div class="eq-math">
     k<sub>+</sub>/k<sub>−</sub> =
     exp(Δμ/RT)
    </div>
    <div class="eq-explain">
     화학적 구동력이 전이의 방향성에 영향을 줘.
     에너지가 없으면 농도 차에 따른 이동만 가능해.
     <div class="eq-value" id="energyResult"></div>
    </div>
   </div>

  </div>
 </div>

 <div class="workarea">

  <div class="panel">
   <div class="panel-head">01 / 실험 조건 조작</div>
   <div class="controls">

    <div class="control">
     <div class="control-line">
      <span>온도 T</span><span id="tempV"></span>
     </div>
     <input id="temp" type="range" min="278" max="338"
       value="298" step="2">
     <small>분자 상태 변화의 속도 조절</small>
    </div>

    <div class="control">
     <div class="control-line">
      <span>결합 친화도 B</span><span id="bindingV"></span>
     </div>
     <input id="binding" type="range" min="-1" max="3"
       value="1" step="0.1">
     <small>이온 포획과 방출의 상대적인 속도 변경</small>
    </div>

    <div class="control">
     <div class="control-line">
      <span>화학적 구동력 Δμ</span><span id="energyV"></span>
     </div>
     <input id="energy" type="range" min="0" max="12"
       value="6" step="0.5">
     <small>수송 방향을 유도하는 에너지 공급</small>
    </div>

    <div class="control">
     <div class="control-line">
      <span>원수 초기 농도</span><span id="concV"></span>
     </div>
     <input id="conc" type="range" min="0.5" max="6"
       value="3" step="0.5">
     <small>정화할 물의 이온 농도</small>
    </div>

    <div class="control">
     <div class="control-line">
      <span>농축수 초기 농도비</span><span id="ratioV"></span>
     </div>
     <input id="ratio" type="range" min="0.1" max="3"
       value="0.5" step="0.1">
     <small>1보다 크면 농도 차에 역행하는 수송을 연구할 수 있어.</small>
    </div>

    <div class="control">
     <div class="control-line">
      <span>펌프 수</span><span id="countV"></span>
     </div>
     <input id="count" type="range" min="1" max="25"
       value="9" step="1">
     <small>동시에 작동하는 분자 펌프의 수</small>
    </div>

    <button id="reset" style="width:100%">처음 조건으로 다시 실험</button>
   </div>
  </div>

  <div class="panel">
   <div class="panel-head">02 / 3D 분자 펌프 · 실시간 동작</div>
   <div class="stage">
    <div class="stage-tag left">원수<br><b id="leftLabel"></b></div>
    <div class="stage-tag right">농축수<br><b id="rightLabel"></b></div>
    <div id="labMount"></div>
   </div>
   <div class="legend">
    <span><i class="dot" style="background:#4dc9ff"></i>목표 이온</span>
    <span><i class="dot" style="background:#c98aff"></i>분자 고리</span>
    <span><i class="dot" style="background:#ffb464"></i>결합 자리</span>
    <span><i class="dot" style="background:#52dabb"></i>분리막</span>
   </div>
   <div class="lab-actions">
    <button class="primary" id="play">일시정지</button>
    <button id="speed">속도 ×1</button>
    <button id="csv">결과 CSV 저장</button>
   </div>
   <div class="intro-footer">
    드래그: 회전 · 휠: 확대 ·
    표시된 입자 수는 계산 농도의 시각적 표현이야.
   </div>
  </div>

  <div class="panel">
   <div class="panel-head">03 / 실시간 실험 결과</div>
   <div class="stats">
    <div class="stat">
     <div class="stat-label">경과 시간</div>
     <div class="stat-number"><span id="timeOut">0</span>
      <span class="stat-unit">s</span></div>
    </div>
    <div class="stat">
     <div class="stat-label">원수 이온 제거율</div>
     <div class="stat-number"><span id="removalOut">0</span>
      <span class="stat-unit">%</span></div>
    </div>
    <div class="stat">
     <div class="stat-label">오른쪽으로의 순간 순수송량</div>
     <div class="stat-number"><span id="fluxOut">0</span>
      <span class="stat-unit">mM/s</span></div>
    </div>
    <div class="stat">
     <div class="stat-label">펌프 이온 점유율</div>
     <div class="stat-number"><span id="occupancyOut">0</span>
      <span class="stat-unit">%</span></div>
    </div>
    <div class="stat">
     <div class="stat-label">누적 화학적 일의 추정값</div>
     <div class="stat-number"><span id="workOut">0</span>
      <span class="stat-unit">mJ</span></div>
    </div>
    <div class="stat">
     <div class="stat-label">현재 순환 구동력</div>
     <div class="stat-number"><span id="affinityOut">0</span>
      <span class="stat-unit">kJ/mol</span></div>
    </div>
   </div>
  </div>

 </div>

 <div class="details">
  <div class="chart-box">
   <div class="chart-heading">용액 농도의 시간 변화</div>
   <canvas id="chart1"></canvas>
   <div class="chart-note">
    <span style="color:#49c8ff">●</span> 원수
    &nbsp;&nbsp;
    <span style="color:#ffae70">●</span> 농축수
    &nbsp; | &nbsp; 단위: mM
   </div>
  </div>
  <div class="chart-box">
   <div class="chart-heading">순수송량의 시간 변화</div>
   <canvas id="chart2"></canvas>
   <div class="chart-note">
    <span style="color:#5be3b7">●</span>
    농축수로 방출되는 순수송량 (mM/s)
   </div>
  </div>
 </div>

 <div class="learning">
  <h3>04 / 이번 탐구에서 확인할 화학적 원리</h3>
  <p>
   <b>분자 간 상호작용:</b>
   분자 펌프와 이온 사이의 결합 친화도가 달라지면
   이온의 포획과 해리 속도도 달라진다.
  </p>
  <p>
   <b>반응속도와 활성화 에너지:</b>
   온도와 에너지 장벽이 상태 변화 속도에 영향을 주며,
   포획이 빠르다고 해서 전체 수송이 반드시 빨라지지는 않는다.
  </p>
  <p>
   <b>화학 변화와 에너지:</b>
   외부 화학 에너지를 공급하면 농도 차에 거스르는
   물질 수송도 가능해진다. 그러나 이를 위해서는
   에너지 소모를 고려해야 한다.
  </p>
  <p>
   <b>농도:</b>
   원수에서 이온이 이동하면 농도가 감소하고,
   농축수에서는 농도가 증가한다.
   농도 차는 순수송 방향에도 영향을 미친다.
  </p>
  <p class="notice">
   ※ 이 시뮬레이션은 미래 우주용 분자 펌프를 가정한
   교육용 계산 모델이다. 실제 이온의 수화, 막의 전기적
   중성, 이온 선택성, 실제 분자구조를 정량적으로
   재현하지 않는다. 분자 고리의 3D 움직임은
   계산된 상태 확률을 시각화한 것이다.
  </p>
 </div>
</div>

<script type="module">
import * as THREE from "three";
import {OrbitControls} from
 "three/addons/controls/OrbitControls.js";

const $ = id => document.getElementById(id);
const R = 8.314;
const TREF = 298;
const SCALE = 0.012;
const DT = 0.006;

// ============================================
// PART A. 텍스트 노벨
// ============================================

const story = [
 {
  who:"항해 시스템 / ARES",
  text:"서기 2042년. 화성을 향해 항해 중인 탐사선 ARES.\n승무원들은 지구에서 가져온 제한된 물을 반복적으로 회수하고 재활용하고 있다."
 },
 {
  who:"항해 시스템 / 경고",
  text:"[주의] 물 재활용 모듈의 이온 제거 성능 저하가 감지되었습니다.\n회수된 물속의 용존 이온 농도가 설정된 기준을 초과했습니다."
 },
 {
  who:"탑재 화학 연구원",
  text:"물을 되찾는 것만으로는 충분하지 않아.\n용해된 이온은 물 분자와 상호작용하며 용액 속에 남아 있어. 이를 분리하려면 추가적인 정화 과정이 필요하지."
 },
 {
  who:"탑재 화학 연구원",
  text:"역삼투나 이온 교환 같은 기술로 이온을 제거할 수 있지만, 장치의 압력 조건과 소모품, 재생 과정 등을 고려해야 해.\n이번 임무에서는 새로운 보조 정화 기술도 검토하기로 했어."
 },
 {
  who:"항해 시스템 / 연구 제안",
  text:"제안 기술: 선택적 분자 펌프.\n특정 이온과 결합하는 분자기계를 가정하고, 화학적 에너지를 공급해 이온을 한쪽으로 이동시키는 방법이야."
 },
 {
  who:"탑재 화학 연구원",
  text:"하지만 결합이 강하다고 무조건 좋은 건 아니야.\n이온을 너무 약하게 붙잡으면 포획에 실패하고, 너무 강하게 붙잡으면 방출하기 어려울 수 있어. 온도와 공급 에너지까지 고려해야 하지."
 },
 {
  who:"항해 시스템 / 실험 시작",
  text:"분자 펌프의 작동을 계산 모델로 시험하겠습니다.\n온도, 결합 친화도, 화학 에너지, 이온 농도를 직접 조절하여 어떤 조건에서 수송이 유리한지 확인해 주세요."
 }
];

let storyIndex = 0;
let mode = "intro";

function renderStory(){
 const s = story[storyIndex];
 $("speaker").textContent = s.who;
 $("storyText").textContent = s.text;
 $("chapter").textContent =
  `PROLOGUE ${String(storyIndex+1).padStart(2,"0")} / 07`;
 $("nextStory").textContent =
  storyIndex === story.length-1 ? "실험실 입장 →" : "다음 대화 →";
}

$("nextStory").onclick = () => {
 if(storyIndex < story.length-1){
  storyIndex++;
  renderStory();
 } else {
  enterLab();
 }
};
$("skipStory").onclick = enterLab;

function enterLab(){
 mode = "lab";
 $("introScreen").classList.add("hidden");
 $("gameUI").classList.remove("hidden");
 $("topDescription").textContent =
  "우주 물 재활용 실험 · 화학 변인을 조작하여 분자 펌프의 작동을 분석하세요.";
 setupLab();
 setTimeout(()=>{
  resizeLab();
  drawCharts();
 },80);
}

// ============================================
// PART B. Three.js 공통 도구
// ============================================

function material(color,opacity=1){
 return new THREE.MeshPhongMaterial({
  color,
  transparent:opacity<1,
  opacity,
  shininess:80,
  depthWrite:opacity===1
 });
}
function meshBox(w,h,d,color){
 return new THREE.Mesh(new THREE.BoxGeometry(w,h,d),material(color));
}
function ball(radius,color){
 return new THREE.Mesh(
  new THREE.SphereGeometry(radius,16,12),
  material(color)
 );
}
function cylinder(radius,length,color){
 return new THREE.Mesh(
  new THREE.CylinderGeometry(radius,radius,length,16),
  material(color)
 );
}
function lighting(scene){
 scene.add(new THREE.AmbientLight(0xffffff,1.2));
 const key = new THREE.DirectionalLight(0xc3eaff,2.3);
 key.position.set(5,9,8);
 scene.add(key);
 const fill = new THREE.PointLight(0x3ccbbd,24);
 fill.position.set(-5,2,5);
 scene.add(fill);
}

// ============================================
// PART C. 프롤로그 3D 우주선
// ============================================

const introMount = $("viewport");
const shipScene = new THREE.Scene();
shipScene.background = new THREE.Color(0x060c18);

const shipCamera = new THREE.PerspectiveCamera(46,1,0.1,150);
shipCamera.position.set(9,5,11);

const shipRenderer = new THREE.WebGLRenderer({antialias:true});
shipRenderer.setPixelRatio(Math.min(devicePixelRatio,2));
shipRenderer.outputColorSpace = THREE.SRGBColorSpace;
introMount.prepend(shipRenderer.domElement);
lighting(shipScene);

const shipControls = new OrbitControls(shipCamera,shipRenderer.domElement);
shipControls.enableDamping=true;
shipControls.enablePan=false;
shipControls.minDistance=6;
shipControls.maxDistance=25;

const spacecraft = new THREE.Group();
shipScene.add(spacecraft);

// 동체: 길이 방향 X
const body = cylinder(0.68,5.0,0xa7bbc9);
body.rotation.z=Math.PI/2;
spacecraft.add(body);

// 전방 원뿔
const nose = new THREE.Mesh(
 new THREE.ConeGeometry(0.68,1.6,24),
 material(0xddebf5)
);
nose.rotation.z=-Math.PI/2;
nose.position.x=3.25;
spacecraft.add(nose);

// 후방 엔진
for(const z of [-0.35,0.35]){
 const engine=cylinder(0.24,0.65,0x45647d);
 engine.rotation.z=Math.PI/2;
 engine.position.set(-2.8,-0.1,z);
 spacecraft.add(engine);
 const glow=ball(0.20,0x5bdfff);
 glow.position.set(-3.2,-0.1,z);
 spacecraft.add(glow);
}

// 태양전지판
for(const z of [-2.7,2.7]){
 const panel=meshBox(2.25,0.08,3.4,0x1b4e86);
 panel.position.set(-0.3,0,z);
 spacecraft.add(panel);

 const border=new THREE.LineSegments(
  new THREE.EdgesGeometry(panel.geometry),
  new THREE.LineBasicMaterial({color:0x66a8d5})
 );
 border.position.copy(panel.position);
 spacecraft.add(border);

 for(let i=-1;i<=1;i++){
  const stripe=meshBox(0.025,0.09,3.3,0x477ab3);
  stripe.position.set(-0.3+i*0.65,0.05,z);
  spacecraft.add(stripe);
 }
 const support=cylinder(0.045,1.25,0xc2d0db);
 support.rotation.x=Math.PI/2;
 support.position.set(-0.3,0,z>0?0.8:-0.8);
 spacecraft.add(support);
}

// 회전 모듈을 나타내는 고리
const ringHab=new THREE.Mesh(
 new THREE.TorusGeometry(1.12,0.17,14,48),
 material(0x89a6bc)
);
ringHab.rotation.y=Math.PI/2;
ringHab.position.x=-1.1;
spacecraft.add(ringHab);

// 통신 안테나
const dish=new THREE.Mesh(
 new THREE.ConeGeometry(0.52,0.24,24),
 material(0xf3f0dc)
);
dish.position.set(0.9,1.1,0);
spacecraft.add(dish);
const antenna=cylinder(0.045,1.0,0xc7dce8);
antenna.position.set(0.9,0.75,0);
spacecraft.add(antenna);

// 별 배경
const starsGeom=new THREE.BufferGeometry();
const stars=[];
for(let i=0;i<900;i++){
 const a=Math.random()*Math.PI*2;
 const z=Math.random()*2-1;
 const r=45+Math.random()*25;
 const q=Math.sqrt(1-z*z);
 stars.push(r*q*Math.cos(a),r*z,r*q*Math.sin(a));
}
starsGeom.setAttribute(
 "position",new THREE.Float32BufferAttribute(stars,3)
);
const starPoints=new THREE.Points(
 starsGeom,
 new THREE.PointsMaterial({
  color:0xdde8ff,size:0.14,sizeAttenuation:true
 })
);
shipScene.add(starPoints);

// 화성
const mars=ball(2.3,0xb85839);
mars.position.set(-11,-5,-17);
shipScene.add(mars);

// ============================================
// PART D. 화학 계산 모델
// ============================================

let running=true;
let speed=1;
let time=0, left=3, right=1.5, initialLeft=3;
let work=0, flux=0;
let state=[1,0,0,0];
let history=[];
let lastSample=0;

function params(){
 return {
  T:+$("temp").value,
  B:+$("binding").value,
  E:+$("energy").value,
  C:+$("conc").value,
  ratio:+$("ratio").value,
  N:+$("count").value
 };
}

// 상태 0: 빈 펌프, 원수 쪽
// 상태 1: 원수 이온 포획
// 상태 2: 이온의 막 반대편 이동
// 상태 3: 이온 방출 뒤 빈 펌프
//
// 순환: 0 -> 1 -> 2 -> 3 -> 0
// 역방향 전이도 모두 허용한다.
//
// 모형의 평형 상수와 상태 전이는
// 교육용 가정으로 설정한다.

function rates(){
 const p=params();
 const thermal=Math.exp(
  -18000/R*(1/p.T-1/TREF)
 );

 const kon=0.15*Math.exp(0.55*p.B)*thermal;
 const koff=0.50*Math.exp(-0.55*p.B)*thermal;
 const trans=0.65*Math.exp(-0.08*p.B*p.B)*thermal;
 const reset=0.8*thermal;
 const drive=p.E*1000/(2*R*p.T);

 return {
  forward:[
   kon*left,
   trans*Math.exp(drive),
   koff,
   reset
  ],
  reverse:[
   koff,
   trans*Math.exp(-drive),
   kon*right,
   reset
  ],
  thermal,kon,koff
 };
}

function step(dt){
 const p=params();
 const rt=rates();
 const f=[],b=[];

 for(let i=0;i<4;i++){
  f[i]=state[i]*rt.forward[i];
  b[i]=state[(i+1)%4]*rt.reverse[i];
 }

 // 현재 상태에 존재하는 확률 이상이
 // 한 번에 유출되지 않도록 제한
 for(let i=0;i<4;i++){
  const prev=(i+3)%4;
  const out=f[i]+b[prev];
  if(out*dt>state[i]&&out>0){
   const scale=state[i]/(out*dt);
   f[i]*=scale;
   b[prev]*=scale;
  }
 }

 // 저장조의 이온 보존
 const useL=f[0]*p.N*SCALE*dt;
 if(useL>left&&useL>0)f[0]*=left/useL;

 const useR=b[2]*p.N*SCALE*dt;
 if(useR>right&&useR>0)b[2]*=right/useR;

 const delta=[0,0,0,0];

 for(let i=0;i<4;i++){
  const next=(i+1)%4;
  const amount=(f[i]-b[i])*dt;
  delta[i]-=amount;
  delta[next]+=amount;
 }

 for(let i=0;i<4;i++){
  state[i]=Math.max(0,state[i]+delta[i]);
 }

 const sum=state.reduce((a,b)=>a+b,0);
 state=state.map(x=>x/sum);

 left=Math.max(0,
  left-(f[0]-b[0])*p.N*SCALE*dt
 );
 right=Math.max(0,
  right+(f[2]-b[2])*p.N*SCALE*dt
 );

 flux=(f[2]-b[2])*p.N*SCALE;

 // 화학 구동 전이의 순반응 진행량을
 // 이용한 이상적 화학적 일
 work+=(f[1]-b[1])*p.N*SCALE*dt*p.E;

 time+=dt;
}

function reset(){
 const p=params();
 time=0;
 left=p.C;
 right=p.C*p.ratio;
 initialLeft=left;
 state=[1,0,0,0];
 work=0;
 flux=0;
 history=[];
 lastSample=0;
 updateLabels();
 updateNumbers();
 sample();
 syncParticles();
 drawCharts();
}

function updateLabels(){
 const p=params();
 $("tempV").textContent=p.T+" K";
 $("bindingV").textContent=p.B.toFixed(1);
 $("energyV").textContent=p.E.toFixed(1)+" kJ/mol";
 $("concV").textContent=p.C.toFixed(1)+" mM";
 $("ratioV").textContent=p.ratio.toFixed(1);
 $("countV").textContent=p.N;

 const rt=rates();
 $("bindingResult").textContent=
  "포획 계수: "+rt.kon.toFixed(3)+
  " / 해리 계수: "+rt.koff.toFixed(3);
 $("tempResult").textContent=
  "298 K 대비 전이속도 배율: "+
  rt.thermal.toFixed(2)+"배";
 $("energyResult").textContent=
  "정·역방향 전이 비: "+
  Math.exp(p.E*1000/(R*p.T)).toFixed(2)+"배";
}

function updateNumbers(){
 const p=params();
 const removal=100*(initialLeft-left)/initialLeft;
 const affinity=p.E-
  R*p.T/1000*Math.log(
   Math.max(right,1e-9)/Math.max(left,1e-9)
  );

 $("timeOut").textContent=time.toFixed(1);
 $("removalOut").textContent=removal.toFixed(1);
 $("fluxOut").textContent=flux.toFixed(3);
 $("occupancyOut").textContent=
  (100*(state[1]+state[2])).toFixed(1);
 $("workOut").textContent=work.toFixed(3);
 $("affinityOut").textContent=affinity.toFixed(2);
 $("leftLabel").textContent=left.toFixed(2)+" mM";
 $("rightLabel").textContent=right.toFixed(2)+" mM";
}

function sample(){
 history.push({
  t:time,
  left,right,flux,work,
  occupied:state[1]+state[2]
 });
 if(history.length>650)history.shift();
}

// ============================================
// PART E. 분자 펌프 3D 환경
// ============================================

let labReady=false;
let labScene,labCamera,labRenderer,labControls;
const pumpObjects=[];
const leftIons=[],rightIons=[];
let labClock=0;

function setupLab(){
 if(labReady)return;
 labReady=true;

 const mount=$("labMount");
 labScene=new THREE.Scene();
 labScene.background=new THREE.Color(0x091522);
 labCamera=new THREE.PerspectiveCamera(48,1,0.1,100);
 labCamera.position.set(8,6,11);

 labRenderer=new THREE.WebGLRenderer({antialias:true});
 labRenderer.setPixelRatio(Math.min(devicePixelRatio,2));
 labRenderer.outputColorSpace=THREE.SRGBColorSpace;
 mount.appendChild(labRenderer.domElement);

 labControls=new OrbitControls(
  labCamera,labRenderer.domElement
 );
 labControls.enableDamping=true;
 labControls.minDistance=5;
 labControls.maxDistance=23;

 lighting(labScene);

 // 저장조 경계
 for(const x of [-2.1,2.1]){
  const box=new THREE.BoxGeometry(4.1,5.3,6.3);
  const edges=new THREE.EdgesGeometry(box);
  const line=new THREE.LineSegments(
   edges,
   new THREE.LineBasicMaterial({
    color:0x557189,transparent:true,opacity:0.55
   })
  );
  line.position.x=x;
  labScene.add(line);
 }

 // 반투명 막
 const membrane=new THREE.Mesh(
  new THREE.BoxGeometry(0.12,5.3,6.3),
  new THREE.MeshPhongMaterial({
   color:0x2bb99a,transparent:true,
   opacity:0.17,depthWrite:false
  })
 );
 labScene.add(membrane);

 // 분자 펌프: 축과 이동하는 고리
 for(let i=0;i<25;i++){
  const row=Math.floor(i/5);
  const col=i%5;

  const group=new THREE.Group();
  group.position.set(
   0,(row-2)*1.04,(col-2)*1.2
  );

  const axle=cylinder(0.065,1.4,0xa7bbd0);
  axle.rotation.z=Math.PI/2;
  group.add(axle);

  const site1=ball(0.13,0xffb464);
  site1.position.x=-0.4;
  group.add(site1);

  const site2=ball(0.13,0x5ce2b7);
  site2.position.x=0.4;
  group.add(site2);

  const ring=new THREE.Mesh(
   new THREE.TorusGeometry(0.22,0.065,12,30),
   material(0xc98aff)
  );
  ring.rotation.y=Math.PI/2;
  group.add(ring);

  const cargo=ball(0.10,0x4dc9ff);
  group.add(cargo);

  labScene.add(group);
  pumpObjects.push({
   group,ring,cargo,
   phase:Math.random()*6.28,
   state:0
  });
 }

 function newIon(color,side){
  const obj=ball(0.085,color);
  obj.userData={
   vx:(Math.random()-.5)*0.018,
   vy:(Math.random()-.5)*0.018,
   vz:(Math.random()-.5)*0.018
  };
  obj.position.set(
   (side==="L"?-1:1)*(0.3+Math.random()*3.7),
   (Math.random()-.5)*4.8,
   (Math.random()-.5)*5.8
  );
  labScene.add(obj);
  return obj;
 }

 for(let i=0;i<100;i++){
  leftIons.push(newIon(0x4dc9ff,"L"));
  rightIons.push(newIon(0xffb470,"R"));
 }

 resizeLab();
 syncParticles();
}

function syncParticles(){
 if(!labReady)return;

 const nL=Math.min(100,Math.round(left*17));
 const nR=Math.min(100,Math.round(right*17));

 leftIons.forEach((o,i)=>o.visible=i<nL);
 rightIons.forEach((o,i)=>o.visible=i<nR);
}

function animateParticles(arr,side){
 const thermal=Math.sqrt(params().T/TREF);

 for(const obj of arr){
  if(!obj.visible)continue;
  const d=obj.userData;

  d.vx=d.vx*.90+(Math.random()-.5)*.007*thermal;
  d.vy=d.vy*.90+(Math.random()-.5)*.007*thermal;
  d.vz=d.vz*.90+(Math.random()-.5)*.007*thermal;

  obj.position.x+=d.vx;
  obj.position.y+=d.vy;
  obj.position.z+=d.vz;

  if(side==="L"){
   if(obj.position.x>-.22||obj.position.x< -4.1){
    d.vx*=-1;
    obj.position.x=Math.min(-.25,Math.max(-4.05,obj.position.x));
   }
  }else{
   if(obj.position.x<.22||obj.position.x>4.1){
    d.vx*=-1;
    obj.position.x=Math.max(.25,Math.min(4.05,obj.position.x));
   }
  }
  if(Math.abs(obj.position.y)>2.5)d.vy*=-1;
  if(Math.abs(obj.position.z)>3.0)d.vz*=-1;
 }
}

function chooseState(){
 let r=Math.random(),c=0;
 for(let i=0;i<4;i++){
  c+=state[i];
  if(r<=c)return i;
 }
 return 3;
}

function animatePumps(t){
 const n=params().N;
 pumpObjects.forEach((p,i)=>{
  p.group.visible=i<n;
  if(i>=n)return;

  if(Math.random()<0.025)p.state=chooseState();

  const positions=[-.65,-.40,.40,.65];
  const target=positions[p.state];
  p.ring.position.x+=(target-p.ring.position.x)*.13;

  p.ring.rotation.x=Math.sin(t*2+p.phase)*.17;
  p.ring.rotation.z=Math.cos(t*1.3+p.phase)*.1;

  p.cargo.visible=p.state===1||p.state===2;
  p.cargo.position.x=p.ring.position.x;
 });
}

function resizeLab(){
 if(!labReady)return;
 const mount=$("labMount");
 const w=Math.max(1,mount.clientWidth);
 const h=Math.max(1,mount.clientHeight);
 labCamera.aspect=w/h;
 labCamera.updateProjectionMatrix();
 labRenderer.setSize(w,h);
}

// ============================================
// PART F. 그래프
// ============================================

function chart(id,series){
 const canvas=$(id);
 const ctx=canvas.getContext("2d");
 const w=canvas.clientWidth;
 const h=canvas.clientHeight;
 const dpr=Math.min(devicePixelRatio,2);

 canvas.width=Math.round(w*dpr);
 canvas.height=Math.round(h*dpr);
 ctx.setTransform(dpr,0,0,dpr,0,0);
 ctx.clearRect(0,0,w,h);

 const L=47,Rpad=12,Tpad=13,Bpad=27;
 const xmin=history.length?history[0].t:0;
 const xmax=Math.max(xmin+1,time);

 const vals=series.flatMap(s=>history.map(d=>s.get(d)));
 const minY=Math.min(0,...vals);
 const maxY=Math.max(0.01,...vals);
 const span=Math.max(.01,maxY-minY);

 const xp=t=>L+(t-xmin)/(xmax-xmin)*(w-L-Rpad);
 const yp=v=>Tpad+(1-(v-minY)/span)*(h-Tpad-Bpad);

 ctx.font="10px Arial";
 ctx.fillStyle="#9bb0c5";
 ctx.strokeStyle="#304559";
 ctx.lineWidth=1;

 for(let i=0;i<=4;i++){
  const y=Tpad+(h-Tpad-Bpad)*i/4;
  ctx.beginPath();
  ctx.moveTo(L,y);
  ctx.lineTo(w-Rpad,y);
  ctx.stroke();
  const value=maxY-span*i/4;
  ctx.fillText(value.toFixed(2),3,y+3);
 }

 ctx.fillText(xmin.toFixed(0),L,h-7);
 ctx.fillText(xmax.toFixed(0)+" s",w-40,h-7);

 for(const s of series){
  ctx.strokeStyle=s.color;
  ctx.lineWidth=2;
  ctx.beginPath();
  history.forEach((d,i)=>{
   const x=xp(d.t),y=yp(s.get(d));
   if(i===0)ctx.moveTo(x,y);
   else ctx.lineTo(x,y);
  });
  ctx.stroke();
 }
}

function drawCharts(){
 if(mode!=="lab")return;
 chart("chart1",[
  {color:"#49c8ff",get:d=>d.left},
  {color:"#ffae70",get:d=>d.right}
 ]);
 chart("chart2",[
  {color:"#5be3b7",get:d=>d.flux}
 ]);
}

// ============================================
// PART G. 조작 및 화학식 강조
// ============================================

function highlight(id){
 ["eq-binding","eq-temp","eq-energy"].forEach(x=>{
  $(x).classList.toggle("active",x===id);
 });
}

$("temp").addEventListener("input",()=>{
 updateLabels();highlight("eq-temp");
});
$("binding").addEventListener("input",()=>{
 updateLabels();highlight("eq-binding");
});
$("energy").addEventListener("input",()=>{
 updateLabels();highlight("eq-energy");
});

// 펌프 수와 초기 농도는 초기 조건이므로 재시작
["conc","ratio","count"].forEach(id=>{
 $(id).addEventListener("change",reset);
 $(id).addEventListener("input",updateLabels);
});

$("reset").onclick=reset;
$("play").onclick=()=>{
 running=!running;
 $("play").textContent=running?"일시정지":"재생";
};

$("speed").onclick=()=>{
 speed=speed===1?2:speed===2?4:1;
 $("speed").textContent="속도 ×"+speed;
};

$("csv").onclick=()=>{
 const p=params();
 const headers=[
  "time_s","left_mM","right_mM",
  "flux_mM_s","work_mJ","occupied",
  "temperature_K","binding_B","driving_kJ_mol","pumps"
 ];
 const rows=history.map(d=>[
  d.t,d.left,d.right,d.flux,d.work,d.occupied,
  p.T,p.B,p.E,p.N
 ]);

 const csv=[headers.join(","),
  ...rows.map(row=>row.join(","))
 ].join("\n");

 const blob=new Blob(["\uFEFF"+csv],{
  type:"text/csv;charset=utf-8"
 });
 const url=URL.createObjectURL(blob);
 const link=document.createElement("a");
 link.href=url;
 link.download="molecular_pump_experiment.csv";
 document.body.appendChild(link);
 link.click();
 link.remove();
 setTimeout(()=>URL.revokeObjectURL(url),1000);
};

// ============================================
// PART H. 메인 애니메이션 루프
// ============================================

function resizeIntro(){
 const w=introMount.clientWidth;
 const h=introMount.clientHeight;
 shipCamera.aspect=w/h;
 shipCamera.updateProjectionMatrix();
 shipRenderer.setSize(w,h);
}

window.addEventListener("resize",()=>{
 if(mode==="intro")resizeIntro();
 else{resizeLab();drawCharts();}
});

let previous=performance.now();
let visualCounter=0;
let chartCounter=0;

function animate(now){
 requestAnimationFrame(animate);
 const delta=Math.min((now-previous)/1000,.05);
 previous=now;

 if(mode==="intro"){
  spacecraft.rotation.y+=delta*.045;
  spacecraft.rotation.z=Math.sin(now*.0004)*.03;
  shipControls.update();
  shipRenderer.render(shipScene,shipCamera);
  return;
 }

 if(!labReady)return;

 if(running){
  const simDt=delta*speed;
  const steps=Math.max(1,Math.ceil(simDt/DT));

  for(let i=0;i<steps;i++){
   step(simDt/steps);
  }

  visualCounter+=delta;
  chartCounter+=delta;

  if(visualCounter>.035){
   labClock+=visualCounter;
   animateParticles(leftIons,"L");
   animateParticles(rightIons,"R");
   animatePumps(labClock);
   visualCounter=0;
  }

  if(chartCounter>.35){
   sample();
   updateNumbers();
   updateLabels();
   syncParticles();
   drawCharts();
   chartCounter=0;
  }
 }

 labControls.update();
 labRenderer.render(labScene,labCamera);
}

renderStory();
resizeIntro();
reset();
requestAnimationFrame(animate);
</script>
</body>
</html>
"""

components.html(HTML, height=1130, scrolling=True)
