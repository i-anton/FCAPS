#!/bin/bash
cd $(dirname "$0")
cbp2make -in Sofia-PS/sofia-ps.cbp -out Sofia-PS/makefile -targets "Debug,Release" -unix
cbp2make -in Sofia-PS/sofia-ps.cbp -out Sofia-PS/makefile.win -targets "Debug,Release" -windows
