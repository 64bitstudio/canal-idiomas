// Bootstrap (ticket 000): placeholder mínimo, mismo patrón inicial que
// mail-core-mc. Este proyecto corre local en la Mac del PO (no se
// despliega), por eso deploy: false. Cuando exista código testeable
// (ticket 002/003), se agrega buildAndTest CON el paso de SonarQube desde
// el inicio: corePipeline corre waitForQualityGate siempre que
// buildAndTest no sea null.
@Library('platform') _

corePipeline(
    projectName: 'canal-idiomas',
    deploy: false
)
