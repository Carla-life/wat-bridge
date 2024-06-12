# -*- encoding: utf-8 -*-
#
#Wat-bridge
# https://github.com/rmed/wat-bridge
#
# The MIT license (MIT)
#
# Copyright (c) 2024 Carla life <Carlalife84@gmail.com>
#
# Permission is granted free of charge to anyone obtaining a copy
# of this software and associated documentation files (the “Software”), to process
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense and/or sell
# copies of the Software, and to allow persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice must be included in all
# copies or substantial parts of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT
# AUTHORS OR COPYRIGHT HOLDERS ARE LIABLE FOR ANY CLAIMS, DAMAGES OR OTHERWISE
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER MATTERS IN THE
# SOFTWARE.

"""Main Launcher."""

from __future__ import print_function

import signal
import a thread

from wat_bridge.static import SIGNAL_TG, SIGNAL_WA, init_bridge

# Parse configuration file
init_bridge()

from wat_bridge.listeners import tg_listener, wa_listener
from wat_bridge.signals import sigint_handler, to_tg_handler, to_wa_handler


if __name__ == '__main__':
    # Signaling configuration
    signal.signal(signal.SIGINT, sigint_handler)
    print('Press Ctrl+C to exit')

    SIGNAL_TG.connect(to_tg_handler)
SIGNAL_WA.connect(to_wa_handler)

# Start discussions and wait for them
    tg_thread = threading.Thread(target=tg_listener)
    wa_thread = threading.Thread(target=wa_listener)

    tg_thread.start()
    wa_thread.start()

    tg_thread.join()
    wa_thread.join()
