/* Object Distructuring Assignment (객체 구조 분해 할당) */

// [ 기본 문법 ]
let toy = {
    productName: '티니핑 인형',
    color: '분홍',
    price: 35000
};

// 프로퍼티 key (순서 무관)
let {productName, color, price} = toy;
console.log(`${productName}은 ${color}색이고 ${price}원이다...`);

// 별칭 부여
let {productName: pn, color: co, price: pr} = toy;
console.log(`${pn}은 ${co}색이고 ${pr}원이다...`);

// 일부 추출
let {productName: pname} = toy;
console.log(`${pname} 사러 갈래...?`);

// 기본값 설정
let {productName: pron, color: col, price: prc, subName: sub='하츄핑'} = toy;
console.log(`${pron}중에서도 ${sub}은 ${col}색이고 ${prc}원이다...`);



// 활용: rest parameters와 조합
let {productName: prn, ...rest} = toy;
console.log(prn);
console.log(rest);

// 만약 let 없이 쓴다면?
let product_name, color_, price_;

({productName: product_name, color: color_, price: price_} = toy);
console.log(product_name, color_, price_);
