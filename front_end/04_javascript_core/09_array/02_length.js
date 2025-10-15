/* array property: length */

const arr = [1, 2, 3, 4, 5];
console.log(arr.length);

// length 프로퍼티는 동적으로 갱신됨
arr.push(6);
console.log(arr.length);
arr.pop();
console.log(arr.length);



// length를 기존 길이보다 작게 조정하면 배열 요소도 조정됨
console.log(arr);
arr.length = 3;
console.log(arr);

// length를 기존 길이보다 늘이면 빈 공간이 추가됨
arr.length = 7;
console.log(arr);



// JS는 배열 요소 일부가 비어있는 배열을 문법적으로 인정함
// 문법적으로 인정 == length로 요소 개수를 셀 때도 카운트
// 단, 요소가 존재하는 것은 아니므로 property에는 없음
const arr2 = [1, , , , 100];
console.log(arr2);
console.log(arr2.length);
console.log(Object.getOwnPropertyDescriptors(arr2));
