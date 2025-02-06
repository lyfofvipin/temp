pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Body matches string", function () {
    pm.expect(pm.response.text()).to.include("kernel-2.6.9-5");
});

pm.test("Your test name", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.RHEL["4.0"].ga[0]).to.eql("kernel-2.6.9-5");
});

pm.test("Status code name has string", function () {
    pm.response.to.have.status("OK");
});

var schema = {
    "type": "object",
    "RHEL": {
        "type": "object"
    }
};

pm.test('Schema is valid', function () {
    
    var jsonData = pm.response.json();
    pm.expect(tv4.validate(jsonData, schema)).to.be.true;
});

pm.test("Successful POST request", function () {
    pm.expect(pm.response.code).to.be.oneOf([200, 202]);
});


