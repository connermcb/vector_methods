
"""
Operations on vectors library
"""

import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def addition(self, v):
        return [x+y for x, y in zip(self.coordinates, v)]
    
    def subtraction(self, v):
        return [x-y for x, y in zip(self.coordinates, v)]
        
    def scalar_mult(self, s):
        return [x*s for x in self.coordinates]
        
    def magnitude(self):
        return math.sqrt(sum([x**2 for x in self.coordinates]))
    
    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance
    
    def unit_vector(self):
        return Vector(self.scalar_mult(1/self.magnitude()))
        
    def dot_product(self, v):
        return sum([x*y for x, y in zip(self.coordinates, v)])
        
    def radians_to_degrees(r):
        return (r*180)/math.pi
    
    def angle(self, v, radians=True):
        a = math.acos(self.dot_product(self.coordinates, v)/(self.magnitude()*v.magnitude()))
        if radians:
            return a
        return self.radians_to_degrees(a)
        
    def is_orthogonal(self, v, tolerance=1e-10):
        return self.dot_product(v) < tolerance
        
    def is_parallel(self, v):
        return (self.is_zero() or v.is_zero() or 
                self.angle(v) == 0 or self.angle(v) == math.pi)
        
    
    def projection(self, b):
        return b.scalar_mult(self.dot_product(b.coordinates))
        
    def parallel_component(self, b):
        try:
            b_unit_vec = b.unit_vector()
            par_component = b_unit_vec.scalar_mult(self.dot_product(b_unit_vec.coordinates))
            return par_component
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e
    
    def orthogonal_component(self, b):
        try:
            parl_comp = self.parallel_component(b)

            return self.subtraction(parl_comp)
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e
            
  
    def cross_product(self, v):
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = v.coordinates
        return Vector([y1*z2 - y2*z1,
                       -(x1*z2 - x2*z1),
                       x1*y2 - x2*y1])

    def cp_area(self, v, triangle=False):
        area = self.cross_product(v).magnitude()
        if triangle:
            return area/2.0
        return area
                
v = Vector([1.5, 9.547, 3.691])
w = Vector([-6.007, 0.124, 5.772])


print(v.cp_area(w))
print(v.cp_area(w, triangle=True))

            
            
            
            
            
            
            
            
            
            
            
            
            
            