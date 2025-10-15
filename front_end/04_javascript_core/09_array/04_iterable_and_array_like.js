/* iterable & array-like */

/*
    iterable: Symbol.iterator 메서드가 구현된 객체
    array-like(유사배열): 인덱스와 length 프로퍼티가 있어 배열처럼 보이는 객체

    - 이터러블이면서 유사배열일 수 있고
    - 이터러블 객체라고 해서 유사배열 객체는 아니며
    - 유사배열 객체라고 해서 이터러블 객체인 것도 아니다.
*/

// 유사배열 객체
let arrayLike = {
    0: '배열인듯',
    1: '배열아닌',
    2: '배열같은',
    3: '유사배열',
    length: 4
};
// console.log(arrayLike.pop());



// 이터러블 객체 (Symbol.iterator 구현)
let range = {
    from: 1,
    to: 5
};

range[Symbol.iterator] = function() {
    return {
        current: this.from,
        last: this.to,
        next() {
            if(this.current <= this.last) {
                return {done: false, value: this.current++};
            } else {
                return {done: true};
            }
        }
    };
};

console.log(range);

for(let item of range) {
    console.log(item);
}

// console.log(range.pop());



/*
    이터러블이나 유사배열을 Array.from()의 인자로 넘겨주면
    새로운 배열을 만들고 객체의 모든 요소를 새롭게 만든 배열에 복사한다.
*/
let arrLikeArr = Array.from(arrayLike);
console.log(arrLikeArr.pop());

let iterArr = Array.from(range);
console.log(iterArr.pop());

// 배열로 생성하기 전 적용할 함수 매핑 가능
iterArr = Array.from(range, num => num * num);
console.log(iterArr);
