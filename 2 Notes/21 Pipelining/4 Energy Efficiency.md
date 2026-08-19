Before, the goal was purely increasing performance on chips, and energy was neglected mostly.

And... across all domains, power became a limit during the early 2000s, and came the energy 'iron law' as well (beside the performance iron law).

![[Screenshot 2026-07-25 at 11.52.53 AM.jpg|400]]

For decades, shrinking transistors let voltage V scale down each generation, keeping energy in check even as instruction counts grew

- That's stalled: pushing V lower now increases leakage power, since transistors stop switching fully off and start behaving more like dimmers than switches
- Capacitance C isn't shrinking as fast either, since transistor sizes aren't scaling down generation-to-generation the way they used to (motivating the move to 3D stacking)

With neither knob giving easy wins anymore, power hit a hard limit, the "power wall", forcing chip design to treat energy efficiency as a first-class constraint alongside raw performance.