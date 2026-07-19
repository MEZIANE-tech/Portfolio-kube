const observer = new IntersectionObserver((entries) => {
    for (const entry of entries){
        console.log(entry.target);
        if(entry.isIntersecting){

            let sheet = document.styleSheets[0];

            const newRuleInfra = ".infra { animation: progressbar_infra 3s cubic-bezier(0, 0, 0.19, 0.97) forwards; }";
            sheet.insertRule(newRuleInfra, sheet.cssRules.length);

            const newRuleDev = ".dev { animation: progressbar_dev 4s cubic-bezier(0, 0, 0.19, 0.97) forwards; }";
            sheet.insertRule(newRuleDev, sheet.cssRules.length);

            const newRuleSecu = ".secu { animation: progressbar_secu 4s cubic-bezier(0, 0, 0.19, 0.97) forwards; }";
            sheet.insertRule(newRuleSecu, sheet.cssRules.length);

            const newRuleLorem = ".Lorem { animation: progressbar_Lorem 3s cubic-bezier(0, 0, 0.19, 0.97) forwards; }";
            sheet.insertRule(newRuleLorem, sheet.cssRules.length);


        }
    }
})


observer.observe(document.querySelector(".progress-bar"))