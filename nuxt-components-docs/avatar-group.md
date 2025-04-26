<!-- source: https://ui.nuxt.com/components/avatar-group --> # AvatarGroup

[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/AvatarGroup.vue)

Stack multiple avatars in a group.

## Usage

Wrap multiple [Avatar](/components/avatar) within an AvatarGroup to stack
them.

    
    
    <template>
      <UAvatarGroup>
        <UAvatar src="https://github.com/benjamincanac.png" alt="Benjamin Canac" />
        <UAvatar src="https://github.com/romhml.png" alt="Romain Hamel" />
        <UAvatar src="https://github.com/noook.png" alt="Neil Richter" />
      </UAvatarGroup>
    </template>
    

### Size

Use the `size` prop to change the size of all the avatars.

size

xl

    
    
    <template>
      <UAvatarGroup size="xl">
        <UAvatar src="https://github.com/benjamincanac.png" alt="Benjamin Canac" />
        <UAvatar src="https://github.com/romhml.png" alt="Romain Hamel" />
        <UAvatar src="https://github.com/noook.png" alt="Neil Richter" />
      </UAvatarGroup>
    </template>
    

### Max

Use the `max` prop to limit the number of avatars displayed. The rest is
displayed as an `+X` avatar.

max

+1

    
    
    <template>
      <UAvatarGroup :max="2">
        <UAvatar src="https://github.com/benjamincanac.png" alt="Benjamin Canac" />
        <UAvatar src="https://github.com/romhml.png" alt="Romain Hamel" />
        <UAvatar src="https://github.com/noook.png" alt="Neil Richter" />
      </UAvatarGroup>
    </template>
    

## Examples

### With tooltip

Wrap each avatar with a [Tooltip](/components/tooltip) to display a tooltip on
hover.

![Neil Richter](https://github.com/noook.png)![Romain
Hamel](https://github.com/romhml.png)![Benjamin
Canac](https://github.com/benjamincanac.png)

    
    
    <template>
      <UAvatarGroup>
        <UTooltip text="benjamincanac">
          <UAvatar
            src="https://github.com/benjamincanac.png"
            alt="Benjamin Canac"
          />
        </UTooltip>
    
        <UTooltip text="romhml">
          <UAvatar
            src="https://github.com/romhml.png"
            alt="Romain Hamel"
          />
        </UTooltip>
    
        <UTooltip text="noook">
          <UAvatar
            src="https://github.com/noook.png"
            alt="Neil Richter"
          />
        </UTooltip>
      </UAvatarGroup>
    </template>
    

### With chip

Wrap each avatar with a [Chip](/components/chip) to display a chip around the
avatar.

![Neil Richter](https://github.com/noook.png)

![Romain Hamel](https://github.com/romhml.png)

![Benjamin Canac](https://github.com/benjamincanac.png)

    
    
    <template>
      <UAvatarGroup>
        <UChip inset color="success">
          <UAvatar
            src="https://github.com/benjamincanac.png"
            alt="Benjamin Canac"
          />
        </UChip>
    
        <UChip inset color="warning">
          <UAvatar
            src="https://github.com/romhml.png"
            alt="Romain Hamel"
          />
        </UChip>
    
        <UChip inset color="error">
          <UAvatar
            src="https://github.com/noook.png"
            alt="Neil Richter"
          />
        </UChip>
      </UAvatarGroup>
    </template>
    

### With link

Wrap each avatar with a [Link](/components/link) to make them clickable.

[![Neil
Richter](https://github.com/noook.png)](https://github.com/noook)[![Romain
Hamel](https://github.com/romhml.png)](https://github.com/romhml)[![Benjamin
Canac](https://github.com/benjamincanac.png)](https://github.com/benjamincanac)

    
    
    <template>
      <UAvatarGroup>
        <ULink
          to="https://github.com/benjamincanac"
          target="_blank"
          class="hover:ring-primary transition"
          raw
        >
          <UAvatar
            src="https://github.com/benjamincanac.png"
            alt="Benjamin Canac"
          />
        </ULink>
    
        <ULink
          to="https://github.com/romhml"
          target="_blank"
          class="hover:ring-primary transition"
          raw
        >
          <UAvatar
            src="https://github.com/romhml.png"
            alt="Romain Hamel"
          />
        </ULink>
    
        <ULink
          to="https://github.com/noook"
          target="_blank"
          class="hover:ring-primary transition"
          raw
        >
          <UAvatar
            src="https://github.com/noook.png"
            alt="Neil Richter"
          />
        </ULink>
      </UAvatarGroup>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`size`| `'md'`| ` "md" | "3xs" | "2xs" | "xs" | "sm" | "lg" | "xl" | "2xl" | "3xl"`  
`max`| | ` string | number`The maximum number of avatars to display.  
`ui`| | ` { root?: ClassNameValue; base?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        avatarGroup: {
          slots: {
            root: 'inline-flex flex-row-reverse justify-end',
            base: 'relative rounded-full ring-bg first:me-0'
          },
          variants: {
            size: {
              '3xs': {
                base: 'ring -me-0.5'
              },
              '2xs': {
                base: 'ring -me-0.5'
              },
              xs: {
                base: 'ring -me-0.5'
              },
              sm: {
                base: 'ring-2 -me-1.5'
              },
              md: {
                base: 'ring-2 -me-1.5'
              },
              lg: {
                base: 'ring-2 -me-1.5'
              },
              xl: {
                base: 'ring-3 -me-2'
              },
              '2xl': {
                base: 'ring-3 -me-2'
              },
              '3xl': {
                base: 'ring-3 -me-2'
              }
            }
          },
          defaultVariants: {
            size: 'md'
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
            avatarGroup: {
              slots: {
                root: 'inline-flex flex-row-reverse justify-end',
                base: 'relative rounded-full ring-bg first:me-0'
              },
              variants: {
                size: {
                  '3xs': {
                    base: 'ring -me-0.5'
                  },
                  '2xs': {
                    base: 'ring -me-0.5'
                  },
                  xs: {
                    base: 'ring -me-0.5'
                  },
                  sm: {
                    base: 'ring-2 -me-1.5'
                  },
                  md: {
                    base: 'ring-2 -me-1.5'
                  },
                  lg: {
                    base: 'ring-2 -me-1.5'
                  },
                  xl: {
                    base: 'ring-3 -me-2'
                  },
                  '2xl': {
                    base: 'ring-3 -me-2'
                  },
                  '3xl': {
                    base: 'ring-3 -me-2'
                  }
                }
              },
              defaultVariants: {
                size: 'md'
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
            avatarGroup: {
              slots: {
                root: 'inline-flex flex-row-reverse justify-end',
                base: 'relative rounded-full ring-bg first:me-0'
              },
              variants: {
                size: {
                  '3xs': {
                    base: 'ring -me-0.5'
                  },
                  '2xs': {
                    base: 'ring -me-0.5'
                  },
                  xs: {
                    base: 'ring -me-0.5'
                  },
                  sm: {
                    base: 'ring-2 -me-1.5'
                  },
                  md: {
                    base: 'ring-2 -me-1.5'
                  },
                  lg: {
                    base: 'ring-2 -me-1.5'
                  },
                  xl: {
                    base: 'ring-3 -me-2'
                  },
                  '2xl': {
                    base: 'ring-3 -me-2'
                  },
                  '3xl': {
                    base: 'ring-3 -me-2'
                  }
                }
              },
              defaultVariants: {
                size: 'md'
              }
            }
          }
        })
      ]
    })
    

Expand code

[AvatarAn img element with fallback and Nuxt Image
support.](/components/avatar)[BadgeA short text to represent a status or a
category.](/components/badge)

