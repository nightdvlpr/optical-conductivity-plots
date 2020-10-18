window.onload = () => {
  let plotObj = new Plot();
  plotObj.calculate();
}

class Plot {

  // constructor
  constructor() {
    // initial messages
    console.clear();
    console.log('________________________ Mathematical Simulation ________________________');

    // data members
    this.lambda = 0.2; // λ
    this.theta = 2 * 180; // θ => Random between 0-360
    this.vf = 2.55;
    this.alpha = 14.82;
    this.k = 10; // Math.pow(10, 10);
    this.h = 1;
    this.m = 35.21;
    this.v = this.vf * (1 + this.alpha * Math.pow(this.k, 2));
    this.mu = 0.25; // μ
    this.t = Math.pow(10, -30);
  }

  calculate() {
    // formula
    // let H = (Math.pow(lambda, 2) * Math.pow(v, 2) * Math.pow(k, 2));
    let E0 = (Math.pow(this.h, 2) * Math.pow(this.k, 2)) / (2 * this.m);
    let E_plus = E0 + Math.sqrt((Math.pow(this.v, 2) * Math.pow(this.k, 2) + Math.pow(this.lambda, 2) * Math.pow(this.k, 6) * Math.pow(Math.cos(angleToRadian(3 * this.theta)), 2)));
    let E_minus = E0 - (Math.sqrt((Math.pow(this.v, 2) * Math.pow(this.k, 2) + Math.pow(this.lambda, 2) * Math.pow(this.k, 6) * Math.pow(Math.cos(angleToRadian(3 * this.theta)), 2))));
    let F_E_plus = (1 / (Math.exp((E_minus / this.t) - (this.mu / this.t)) + 1));
    let F_E_minus = (1 / (Math.exp((E_plus / this.t) - (this.mu / this.t)) + 1));
    
    prt("E0 => " + E0);
    prt("E- => " + E_minus);
    prt("E+ => " + E_plus);
    prt("f(E-) => " + F_E_plus);
    prt("f(E+) => " + F_E_minus);
  }
}

// convert angle to radian => (Angle in degrees x PI / 180).
function angleToRadian(angle) {
  return (angle * Math.PI / 180);
}

// print data
function prt(content) {
  console.log('%c' + content, 'color: #ff1493; font-size: 30px;');
}