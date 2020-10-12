window.onload = () => {
  console.clear();
  console.log('________________________ Mathematical Simulation ________________________');

  // data members
  const lambda = .2; //λ
  const theta = 2 * Math.PI; //θ
  const vf = 2.55;
  const alpha = 14.82;
  const k = Math.pow(10, 10);
  const h = 1;
  const m = 32.55;
  let v;

  v = vf * (1 + Math.pow(alpha * k, 2));
  // formula
  // let H = (Math.pow(lambda, 2) * Math.pow(v, 2) * Math.pow(k, 2));

  let E_zero = (Math.pow(h, 2) * Math.pow(k, 2)) / (2 * m);
  let E_plus = E_zero + (Math.sqrt((Math.pow(v, 2) * Math.pow(k, 2) + Math.pow(lambda, 2) * Math.pow(k, 6) * Math.pow(Math.cos(3 * theta), 2))));
  let E_minus = E_zero - (Math.sqrt((Math.pow(v, 2) * Math.pow(k, 2) + Math.pow(lambda, 2) * Math.pow(k, 6) * Math.pow(Math.cos(3 * theta), 2))));

  prt("E0 => " + E_zero);
  prt("E- => " + E_plus);
  prt("E+ => "+E_minus);
}


function prt(content) {
  console.log('%c' + content,'color: #ff1493; font-size: 30px;');
}
