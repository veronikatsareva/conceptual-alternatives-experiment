//
// Define a new "Boxes" controller, which is a combination of a "Message" (the
// boxes) and a "Question" (whether the target box follows the rule).
//
define_ibex_controller({
    name: "Boxes",
    jqueryWidget: {
        _init: function () {
            this.options.transfer = null; // Remove "Click here to continue" message.
            this.element.VBox({
                options: this.options,
                triggers: [1],
                children: [
                    "Message", this.options,
                    "Question", this.options
                ]
            });
        }
    },
    properties: { }
});

var shuffleSequence = seq("consent", "practice", randomize("real"));
var showProgressBar = true;
var completionMessage = "Результаты были успешно отправлены на сервер. Спасибо за участие!"
// var centerItems = false;

var defaults = [
    // "Separator", {
    //     transfer: 1000,
    //     normalMessage: "Please wait for the next item."
    // },
    "Form", {
        continueOnReturn: true,
        saveReactionTime: true
    },
    "Boxes", {
        as: ["Соответствует правилу", "Не соответствует правилу"],
        hasCorrect: false,
        presentHorizontally: true,
        // autoFirstChar: true
    }
];

var items = [

    ["sep", "Separator", { }],

    //
    // Инструкция
    //
    ["consent", "Form", {html: {include: "consent.html"}}],

    //
    // Два тренировочных задания
    //
    ["practice", "Boxes", {html: {include: "practice1.html"}}],
    ["practice", "Boxes", {html: {include: "practice2.html"}}],

    //
    // Задания
    //
    ["real", "Boxes", {html: {include: "test1.html"}}],
    ["real", "Boxes", {html: {include: "test2.html"}}],
    ["real", "Boxes", {html: {include: "test3.html"}}],
    ["real", "Boxes", {html: {include: "test4.html"}}],
    ["real", "Boxes", {html: {include: "test5.html"}}],
    ["real", "Boxes", {html: {include: "test6.html"}}],
    ["real", "Boxes", {html: {include: "test7.html"}}],
    ["real", "Boxes", {html: {include: "test8.html"}}],
    ["real", "Boxes", {html: {include: "test9.html"}}],
    ["real", "Boxes", {html: {include: "test10.html"}}],
    ["real", "Boxes", {html: {include: "test11.html"}}],
    ["real", "Boxes", {html: {include: "test12.html"}}],
    ["real", "Boxes", {html: {include: "test13.html"}}],
    ["real", "Boxes", {html: {include: "test14.html"}}],
    ["real", "Boxes", {html: {include: "test15.html"}}],
    ["real", "Boxes", {html: {include: "test16.html"}}],
    ["real", "Boxes", {html: {include: "test17.html"}}],
    ["real", "Boxes", {html: {include: "test18.html"}}],
];
