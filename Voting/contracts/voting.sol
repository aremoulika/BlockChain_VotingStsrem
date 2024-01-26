// SPDX-License-Identifier: MIT 
pragma solidity 0.8.19;

contract voting {
    int8[3] _votes;

    mapping(address=>bool) _voters;
    function castvote(int8 id) public {

          require(!_voters[msg.sender]);
          if(id==1) {
              _votes[0]+=1;
              // _voters[msg.sender]=true;
          }
          else if(id==2) {
              _votes[1]+=1;
              // _voters[msg.sender]=true;
              }
          else if(id==3) {
              _votes[2]+=1;
              // _voters[msg.sender]=true;
          }
          _voters[msg.sender]=true;
          
    }

    function result() public view returns(int8[3] memory) {
        return(_votes);
    }
}