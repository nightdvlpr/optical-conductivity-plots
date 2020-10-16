window.onload = () => {
  let plotObj = new Plot();
  prt("E0 => " + plotObj.e_zero);
  prt("E- => " + plotObj.e_minus);
  prt("E+ => " + plotObj.e_plus);
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
  }

  calculate() {
    // formula
    // let H = (Math.pow(lambda, 2) * Math.pow(v, 2) * Math.pow(k, 2));
  }

  get e_zero() {
    return this.calc_E_zero();
  }

  get e_plus() {
    return this.calc_E_plus();
  }

  get e_minus() {
    return this.calc_E_minus();
  }

  calc_E_zero() {
    return (Math.pow(this.h, 2) * Math.pow(this.k, 2)) / (2 * this.m);
  }

  calc_E_plus() {
    return (this.e_zero + Math.sqrt((Math.pow(this.v, 2) * Math.pow(this.k, 2) + Math.pow(this.lambda, 2) * Math.pow(this.k, 6) * Math.pow(Math.cos(angleToRadian(3 * this.theta)), 2))));
  }

  calc_E_minus() {
    return (this.e_zero - (Math.sqrt((Math.pow(this.v, 2) * Math.pow(this.k, 2) + Math.pow(this.lambda, 2) * Math.pow(this.k, 6) * Math.pow(Math.cos(angleToRadian(3 * this.theta)), 2)))));
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