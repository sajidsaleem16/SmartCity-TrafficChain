const TrafficReport = artifacts.require("TrafficReport");

module.exports = function (deployer) {
    deployer.deploy(TrafficReport);
};
