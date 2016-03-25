#!/bin/bash
asd=$(aticonfig --odgc)
echo $asd | cut -c166-171 | tr -d %
