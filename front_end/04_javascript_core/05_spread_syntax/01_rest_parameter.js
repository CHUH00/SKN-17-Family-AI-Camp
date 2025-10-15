/* 나머지 매개변수 (Rest Parameter) */

function mergeAll(arg1, arg2, arg3) {
    var msg = '';
    msg = arg1 + arg2 + arg3;
    return msg;
}

console.log(mergeAll('안녕하세요!'));
console.log(mergeAll('안녕하세요!', '반갑습니다~'));
console.log(mergeAll('안녕하세요!', '반갑습니다~', '다람쥐입니다 :)'));
console.log(mergeAll('안녕하세요!', '반갑습니다~', '다람쥐입니다 :)', '화이팅!!!'));

/*
function mergeInformation(nickname, hobby1, hobby2, hobby3) {
    var hobbies = '';
    hobbies = hobby1 + hobby2 + hobby3;
    return `나 ${nickname}, 취미는 ${hobbies}죠!`;
}
*/
function mergeInformation(nickname, ...hobbies) {
    var msg = '';
    for(var hobby of hobbies) {
        msg += hobby;
    }
    return `나 ${nickname}, 취미는 ${msg}죠!`;
}

console.log(mergeInformation('다람쥐', '놀기', '먹기', '자기', '강의하기'));
console.log(mergeInformation('다람쥐', '놀기', '먹기', '자기'));
console.log(mergeInformation('다람쥐', '놀기'));

// 나머지 매개변수는 항상 마지막에 있어야 함
// function func(arg1, arg2, ...args, arg3) {}
