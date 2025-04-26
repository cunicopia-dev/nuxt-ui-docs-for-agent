<!-- source: https://ui.nuxt.com/components/slider --> # Slider

[Slider](https://reka-
ui.com/docs/components/slider)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Slider.vue)

An input to select a numeric value within a range.

## Usage

Use the `v-model` directive to control the value of the Slider.

modelValue

    
    
    <script setup lang="ts">
    const value = ref(50)
    </script>
    
    <template>
      <USlider v-model="value" />
    </template>
    

Use the `default-value` prop to set the initial value when you do not need to
control its state.

    
    
    <template>
      <USlider :default-value="50" />
    </template>
    

### Min / Max

Use the `min` and `max` props to set the minimum and maximum values of the
Slider. Defaults to `0` and `100`.

min

max

    
    
    <template>
      <USlider :min="0" :max="50" :default-value="50" />
    </template>
    

### Step

Use the `step` prop to set the increment value of the Slider. Defaults to `1`.

step

    
    
    <template>
      <USlider :step="10" :default-value="50" />
    </template>
    

### Multiple

Use the `v-model` directive or the `default-value` prop with an array of
values to create a range Slider.

    
    
    <script setup lang="ts">
    const value = ref([
      25,
      75
    ])
    </script>
    
    <template>
      <USlider v-model="value" />
    </template>
    

Use the `min-steps-between-thumbs` prop to limit the minimum distance between
the thumbs.

minStepsBetweenThumbs

    
    
    <script setup lang="ts">
    const value = ref([
      25,
      50,
      75
    ])
    </script>
    
    <template>
      <USlider v-model="value" :min-steps-between-thumbs="10" />
    </template>
    

### Orientation

Use the `orientation` prop to change the orientation of the Slider. Defaults
to `horizontal`.

orientation

vertical

    
    
    <template>
      <USlider orientation="vertical" :default-value="50" class="h-48" />
    </template>
    

### Color

Use the `color` prop to change the color of the Slider.

color

neutral

    
    
    <template>
      <USlider color="neutral" :default-value="50" />
    </template>
    

### Size

Use the `size` prop to change the size of the Slider.

size

xl

    
    
    <template>
      <USlider size="xl" :default-value="50" />
    </template>
    

### Disabled

Use the `disabled` prop to disable the Slider.

disabled

true

    
    
    <template>
      <USlider disabled :default-value="50" />
    </template>
    

### Inverted

Use the `inverted` prop to visually invert the Slider.

inverted

true

    
    
    <template>
      <USlider inverted :default-value="25" />
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`size`| `'md'`| ` "sm" | "md" | "xs" | "lg" | "xl"`  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`orientation`| `'horizontal'`| ` "horizontal" | "vertical"`The orientation of the slider.  
`defaultValue`| | ` number | number[]`The value of the slider when initially rendered. Use when you do not need to control the state of the slider.  
`disabled`| | `boolean`When `true`, prevents the user from interacting with the slider.  
`name`| | ` string`The name of the field. Submitted with its owning form as part of a name/value pair.  
`inverted`| | `boolean`Whether the slider is visually inverted.  
`min`| `0`| ` number`The minimum value for the range.  
`max`| `100`| ` number`The maximum value for the range.  
`step`| `1`| ` number`The stepping interval.  
`minStepsBetweenThumbs`| | ` number`The minimum permitted steps between multiple thumbs.  
`modelValue`| | ` number | number[]`  
`ui`| | ` { root?: ClassNameValue; track?: ClassNameValue; range?: ClassNameValue; thumb?: ClassNameValue; }`  
  
### Emits

Event |  Type   
---|---  
`change`| `[payload: Event]`  
`update:modelValue`| `[payload: number | number[]]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        slider: {
          slots: {
            root: 'relative flex items-center select-none touch-none',
            track: 'relative bg-accented overflow-hidden rounded-full grow',
            range: 'absolute rounded-full',
            thumb: 'rounded-full bg-default ring-2 focus-visible:outline-2 focus-visible:outline-offset-2'
          },
          variants: {
            color: {
              primary: {
                range: 'bg-primary',
                thumb: 'ring-primary focus-visible:outline-primary/50'
              },
              secondary: {
                range: 'bg-secondary',
                thumb: 'ring-secondary focus-visible:outline-secondary/50'
              },
              success: {
                range: 'bg-success',
                thumb: 'ring-success focus-visible:outline-success/50'
              },
              info: {
                range: 'bg-info',
                thumb: 'ring-info focus-visible:outline-info/50'
              },
              warning: {
                range: 'bg-warning',
                thumb: 'ring-warning focus-visible:outline-warning/50'
              },
              error: {
                range: 'bg-error',
                thumb: 'ring-error focus-visible:outline-error/50'
              },
              neutral: {
                range: 'bg-inverted',
                thumb: 'ring-inverted focus-visible:outline-inverted/50'
              }
            },
            size: {
              xs: {
                thumb: 'size-3'
              },
              sm: {
                thumb: 'size-3.5'
              },
              md: {
                thumb: 'size-4'
              },
              lg: {
                thumb: 'size-4.5'
              },
              xl: {
                thumb: 'size-5'
              }
            },
            orientation: {
              horizontal: {
                root: 'w-full',
                range: 'h-full'
              },
              vertical: {
                root: 'flex-col h-full',
                range: 'w-full'
              }
            },
            disabled: {
              true: {
                root: 'opacity-75 cursor-not-allowed'
              }
            }
          },
          compoundVariants: [
            {
              orientation: 'horizontal',
              size: 'xs',
              class: {
                track: 'h-[6px]'
              }
            },
            {
              orientation: 'horizontal',
              size: 'sm',
              class: {
                track: 'h-[7px]'
              }
            },
            {
              orientation: 'horizontal',
              size: 'md',
              class: {
                track: 'h-[8px]'
              }
            },
            {
              orientation: 'horizontal',
              size: 'lg',
              class: {
                track: 'h-[9px]'
              }
            },
            {
              orientation: 'horizontal',
              size: 'xl',
              class: {
                track: 'h-[10px]'
              }
            },
            {
              orientation: 'vertical',
              size: 'xs',
              class: {
                track: 'w-[6px]'
              }
            },
            {
              orientation: 'vertical',
              size: 'sm',
              class: {
                track: 'w-[7px]'
              }
            },
            {
              orientation: 'vertical',
              size: 'md',
              class: {
                track: 'w-[8px]'
              }
            },
            {
              orientation: 'vertical',
              size: 'lg',
              class: {
                track: 'w-[9px]'
              }
            },
            {
              orientation: 'vertical',
              size: 'xl',
              class: {
                track: 'w-[10px]'
              }
            }
          ],
          defaultVariants: {
            size: 'md',
            color: 'primary'
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          ui: {
            slider: {
              slots: {
                root: 'relative flex items-center select-none touch-none',
                track: 'relative bg-accented overflow-hidden rounded-full grow',
                range: 'absolute rounded-full',
                thumb: 'rounded-full bg-default ring-2 focus-visible:outline-2 focus-visible:outline-offset-2'
              },
              variants: {
                color: {
                  primary: {
                    range: 'bg-primary',
                    thumb: 'ring-primary focus-visible:outline-primary/50'
                  },
                  secondary: {
                    range: 'bg-secondary',
                    thumb: 'ring-secondary focus-visible:outline-secondary/50'
                  },
                  success: {
                    range: 'bg-success',
                    thumb: 'ring-success focus-visible:outline-success/50'
                  },
                  info: {
                    range: 'bg-info',
                    thumb: 'ring-info focus-visible:outline-info/50'
                  },
                  warning: {
                    range: 'bg-warning',
                    thumb: 'ring-warning focus-visible:outline-warning/50'
                  },
                  error: {
                    range: 'bg-error',
                    thumb: 'ring-error focus-visible:outline-error/50'
                  },
                  neutral: {
                    range: 'bg-inverted',
                    thumb: 'ring-inverted focus-visible:outline-inverted/50'
                  }
                },
                size: {
                  xs: {
                    thumb: 'size-3'
                  },
                  sm: {
                    thumb: 'size-3.5'
                  },
                  md: {
                    thumb: 'size-4'
                  },
                  lg: {
                    thumb: 'size-4.5'
                  },
                  xl: {
                    thumb: 'size-5'
                  }
                },
                orientation: {
                  horizontal: {
                    root: 'w-full',
                    range: 'h-full'
                  },
                  vertical: {
                    root: 'flex-col h-full',
                    range: 'w-full'
                  }
                },
                disabled: {
                  true: {
                    root: 'opacity-75 cursor-not-allowed'
                  }
                }
              },
              compoundVariants: [
                {
                  orientation: 'horizontal',
                  size: 'xs',
                  class: {
                    track: 'h-[6px]'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'sm',
                  class: {
                    track: 'h-[7px]'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'md',
                  class: {
                    track: 'h-[8px]'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'lg',
                  class: {
                    track: 'h-[9px]'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'xl',
                  class: {
                    track: 'h-[10px]'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'xs',
                  class: {
                    track: 'w-[6px]'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'sm',
                  class: {
                    track: 'w-[7px]'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'md',
                  class: {
                    track: 'w-[8px]'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'lg',
                  class: {
                    track: 'w-[9px]'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'xl',
                  class: {
                    track: 'w-[10px]'
                  }
                }
              ],
              defaultVariants: {
                size: 'md',
                color: 'primary'
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          ui: {
            slider: {
              slots: {
                root: 'relative flex items-center select-none touch-none',
                track: 'relative bg-accented overflow-hidden rounded-full grow',
                range: 'absolute rounded-full',
                thumb: 'rounded-full bg-default ring-2 focus-visible:outline-2 focus-visible:outline-offset-2'
              },
              variants: {
                color: {
                  primary: {
                    range: 'bg-primary',
                    thumb: 'ring-primary focus-visible:outline-primary/50'
                  },
                  secondary: {
                    range: 'bg-secondary',
                    thumb: 'ring-secondary focus-visible:outline-secondary/50'
                  },
                  success: {
                    range: 'bg-success',
                    thumb: 'ring-success focus-visible:outline-success/50'
                  },
                  info: {
                    range: 'bg-info',
                    thumb: 'ring-info focus-visible:outline-info/50'
                  },
                  warning: {
                    range: 'bg-warning',
                    thumb: 'ring-warning focus-visible:outline-warning/50'
                  },
                  error: {
                    range: 'bg-error',
                    thumb: 'ring-error focus-visible:outline-error/50'
                  },
                  neutral: {
                    range: 'bg-inverted',
                    thumb: 'ring-inverted focus-visible:outline-inverted/50'
                  }
                },
                size: {
                  xs: {
                    thumb: 'size-3'
                  },
                  sm: {
                    thumb: 'size-3.5'
                  },
                  md: {
                    thumb: 'size-4'
                  },
                  lg: {
                    thumb: 'size-4.5'
                  },
                  xl: {
                    thumb: 'size-5'
                  }
                },
                orientation: {
                  horizontal: {
                    root: 'w-full',
                    range: 'h-full'
                  },
                  vertical: {
                    root: 'flex-col h-full',
                    range: 'w-full'
                  }
                },
                disabled: {
                  true: {
                    root: 'opacity-75 cursor-not-allowed'
                  }
                }
              },
              compoundVariants: [
                {
                  orientation: 'horizontal',
                  size: 'xs',
                  class: {
                    track: 'h-[6px]'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'sm',
                  class: {
                    track: 'h-[7px]'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'md',
                  class: {
                    track: 'h-[8px]'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'lg',
                  class: {
                    track: 'h-[9px]'
                  }
                },
                {
                  orientation: 'horizontal',
                  size: 'xl',
                  class: {
                    track: 'h-[10px]'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'xs',
                  class: {
                    track: 'w-[6px]'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'sm',
                  class: {
                    track: 'w-[7px]'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'md',
                  class: {
                    track: 'w-[8px]'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'lg',
                  class: {
                    track: 'w-[9px]'
                  }
                },
                {
                  orientation: 'vertical',
                  size: 'xl',
                  class: {
                    track: 'w-[10px]'
                  }
                }
              ],
              defaultVariants: {
                size: 'md',
                color: 'primary'
              }
            }
          }
        })
      ]
    })
    

Expand code

[SlideoverA dialog that slides in from any side of the
screen.](/components/slideover)[StepperA set of steps that are used to
indicate progress through a multi-step process.](/components/stepper)

