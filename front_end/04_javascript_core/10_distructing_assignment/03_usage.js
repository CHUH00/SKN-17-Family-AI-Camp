/* 구조 분해 할당의 활용 */
// QUIZ! ??? 자리 세 곳을 코드로 채워주세요!

/* 중첩 구조 분해 (Nested distructuring) */
let lunchSet = {
    burger: {
        main: '소고기',
        sub: '치즈',
        vegetable: ['양상추', '토마토', '피클']
    },
    side: ['감자튀김', '코울슬로'],
    price: 18000
};

let {burger: {main, sub, vegetable: [vege1, vege2, vege3]}, side: [side1, side2], price} = lunchSet;

console.log(`burger = ${main} + ${sub} + ${vege1} + ${vege2} + ${vege3}`);
console.log(`side = ${side1} & ${side2}`);
console.log(price + '원');



/* 함수 파라미터(Function parameters) 활용 */

// [ 문제상황 ]
// JS 파라미터는 키워드 인자가 없다.
// 따라서 인수의 순서가 고정되며, 기본값을 설정하더라도 undefined로 자리를 맞춰야 한다.
function displayProduct(producer='아무개', width=0, height=0, items=[]) {
    console.log('==============================');
    console.log(`${producer} made`);
    console.log(`${width} x ${height}`);
    console.log(items);
    console.log('==============================');
}

displayProduct('다람쥐', 100, 200, ['도토리', '호두', '밤']);
displayProduct('다람쥐', ['도토리', '밤', '호두']);
displayProduct('다람쥐', undefined, undefined, ['도토리', '밤', '호두']);

// [ 해결방법 ]
// 구조 분해 할당을 이용하면 Python의 키워드 인자처럼 파라미터를 사용할 수 있다.
// '순서도 무관'하고 기본 값을 활용할 때도 '별도의 처리가 필요 없'다.
function displayProductDev({producer='아무개', width=0, height=0, items=[]}) { 
    console.log('==============================');
    console.log(`${producer} made`);
    console.log(`${width} x ${height}`);
    console.log(items);
    console.log('==============================');
}

let example = {
    producer: '다람쥐',
    // width: 100,
    // height: 100,
    items: ["호두", "밤", "도토리"]
};

displayProductDev(example);
