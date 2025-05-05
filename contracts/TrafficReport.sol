// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TrafficReport {
    struct Report {
        address reporter;
        string location;
        string congestionLevel;
        uint timestamp;
        bool verified;
    }

    mapping(uint => Report) public reports;
    uint public reportCount = 0;
    address public admin;

    event NewReport(uint reportId, address reporter, string location, string congestionLevel);
    event ReportVerified(uint reportId, bool verified);

    constructor() {
        admin = msg.sender; // Set contract deployer as admin
    }

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can verify reports");
        _;
    }

    function submitReport(string memory _location, string memory _congestionLevel) public {
        reportCount++;
        reports[reportCount] = Report(msg.sender, _location, _congestionLevel, block.timestamp, false);
        emit NewReport(reportCount, msg.sender, _location, _congestionLevel);
    }

    function verifyReport(uint _reportId) public onlyAdmin {
        require(_reportId > 0 && _reportId <= reportCount, "Invalid report ID");
        reports[_reportId].verified = true;
        emit ReportVerified(_reportId, true);
    }

    function getReport(uint _reportId) public view returns (string memory, string memory, bool) {
        return (reports[_reportId].location, reports[_reportId].congestionLevel, reports[_reportId].verified);
    }
}
