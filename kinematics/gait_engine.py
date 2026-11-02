import math

class QuadrupedKinematics:
    """
    3-DOF Inverse Kinematics and Gait Orchestration Engine for NOBoT
    Author: Mihir Mahato
    """
    def __init__(self, l1_coxa=45.0, l2_femur=75.0, l3_tibia=120.0):
        self.L1 = l1_coxa
        self.L2 = l2_femur
        self.L3 = l3_tibia

    def solve_ik(self, x, y, z):
        """
        Solves joint angles (theta_coxa, theta_femur, theta_tibia) in degrees
        for coordinate target (x, y, z) in mm
        """
        # 1. Coxa rotation
        theta_coxa = math.atan2(y, x)

        # 2. Distance in horizontal plane
        r = math.sqrt(x**2 + y**2) - self.L1
        d = math.sqrt(r**2 + z**2)

        # 3. Law of Cosines for Tibia
        cos_tibia = (self.L2**2 + self.L3**2 - d**2) / (2 * self.L2 * self.L3)
        cos_tibia = max(-1.0, min(1.0, cos_tibia)) # Clamping
        theta_tibia = math.acos(cos_tibia)

        # 4. Law of Cosines for Femur
        alpha = math.atan2(z, r)
        cos_femur = (self.L2**2 + d**2 - self.L3**2) / (2 * self.L2 * d)
        cos_femur = max(-1.0, min(1.0, cos_femur))
        theta_femur = alpha + math.acos(cos_femur)

        return (
            math.degrees(theta_coxa),
            math.degrees(theta_femur),
            math.degrees(theta_tibia)
        )
