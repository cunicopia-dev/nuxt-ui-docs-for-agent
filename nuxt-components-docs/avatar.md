<!-- source: https://ui.nuxt.com/components/avatar --> # Avatar

[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Avatar.vue)

An img element with fallback and Nuxt Image support.

## Usage

The Avatar uses the `<NuxtImg>` component when
[`@nuxt/image`](https://github.com/nuxt/image) is installed, falling back to
`img` otherwise.

You can pass any property from the HTML `<img>` element such as `alt`,
`loading`, etc.

### Src

Use the `src` prop to set the image URL.

src

    
    
    <template>
      <UAvatar src="https://github.com/benjamincanac.png" />
    </template>
    

### Size

Use the `size` prop to set the size of the Avatar.

size

xl

    
    
    <template>
      <UAvatar src="https://github.com/benjamincanac.png" size="xl" />
    </template>
    

The `<img>` element's `width` and `height` are automatically set based on the
`size` prop.

### Icon

Use the `icon` prop to display a fallback [Icon](/components/icon).

icon

size

md

    
    
    <template>
      <UAvatar icon="i-lucide-image" size="md" />
    </template>
    

### Text

Use the `text` prop to display a fallback text.

text

size

md

    
    
    <template>
      <UAvatar text="+1" size="md" />
    </template>
    

### Alt

When no icon or text is provided, the **initials** of the `alt` prop is used
as fallback.

alt

size

md

    
    
    <template>
      <UAvatar alt="Benjamin Canac" size="md" />
    </template>
    

The `alt` prop is passed to the `img` element as the `alt` attribute.

## Examples

### With tooltip

You can use a [Tooltip](/components/tooltip) component to display a tooltip
when hovering the Avatar.

![Benjamin Canac](https://github.com/benjamincanac.png)

    
    
    <template>
      <UTooltip text="Benjamin Canac">
        <UAvatar
          src="https://github.com/benjamincanac.png"
          alt="Benjamin Canac"
        />
      </UTooltip>
    </template>
    

### With chip

You can use a [Chip](/components/chip) component to display a chip around the
Avatar.

![Benjamin Canac](https://github.com/benjamincanac.png)

    
    
    <template>
      <UChip inset>
        <UAvatar
          src="https://github.com/benjamincanac.png"
          alt="Benjamin Canac"
        />
      </UChip>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'span'`| `any`The element or component this component should render as.  
`src`| | ` string`  
`alt`| | ` string`  
`icon`| | ` string`  
`text`| | ` string`  
`size`| `'md'`| ` "md" | "3xs" | "2xs" | "xs" | "sm" | "lg" | "xl" | "2xl" | "3xl"`  
`ui`| | ` { root?: ClassNameValue; image?: ClassNameValue; fallback?: ClassNameValue; icon?: ClassNameValue; }`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        avatar: {
          slots: {
            root: 'inline-flex items-center justify-center shrink-0 select-none overflow-hidden rounded-full align-middle bg-elevated',
            image: 'h-full w-full rounded-[inherit] object-cover',
            fallback: 'font-medium leading-none text-muted truncate',
            icon: 'text-muted shrink-0'
          },
          variants: {
            size: {
              '3xs': {
                root: 'size-4 text-[8px]'
              },
              '2xs': {
                root: 'size-5 text-[10px]'
              },
              xs: {
                root: 'size-6 text-xs'
              },
              sm: {
                root: 'size-7 text-sm'
              },
              md: {
                root: 'size-8 text-base'
              },
              lg: {
                root: 'size-9 text-lg'
              },
              xl: {
                root: 'size-10 text-xl'
              },
              '2xl': {
                root: 'size-11 text-[22px]'
              },
              '3xl': {
                root: 'size-12 text-2xl'
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
            avatar: {
              slots: {
                root: 'inline-flex items-center justify-center shrink-0 select-none overflow-hidden rounded-full align-middle bg-elevated',
                image: 'h-full w-full rounded-[inherit] object-cover',
                fallback: 'font-medium leading-none text-muted truncate',
                icon: 'text-muted shrink-0'
              },
              variants: {
                size: {
                  '3xs': {
                    root: 'size-4 text-[8px]'
                  },
                  '2xs': {
                    root: 'size-5 text-[10px]'
                  },
                  xs: {
                    root: 'size-6 text-xs'
                  },
                  sm: {
                    root: 'size-7 text-sm'
                  },
                  md: {
                    root: 'size-8 text-base'
                  },
                  lg: {
                    root: 'size-9 text-lg'
                  },
                  xl: {
                    root: 'size-10 text-xl'
                  },
                  '2xl': {
                    root: 'size-11 text-[22px]'
                  },
                  '3xl': {
                    root: 'size-12 text-2xl'
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
            avatar: {
              slots: {
                root: 'inline-flex items-center justify-center shrink-0 select-none overflow-hidden rounded-full align-middle bg-elevated',
                image: 'h-full w-full rounded-[inherit] object-cover',
                fallback: 'font-medium leading-none text-muted truncate',
                icon: 'text-muted shrink-0'
              },
              variants: {
                size: {
                  '3xs': {
                    root: 'size-4 text-[8px]'
                  },
                  '2xs': {
                    root: 'size-5 text-[10px]'
                  },
                  xs: {
                    root: 'size-6 text-xs'
                  },
                  sm: {
                    root: 'size-7 text-sm'
                  },
                  md: {
                    root: 'size-8 text-base'
                  },
                  lg: {
                    root: 'size-9 text-lg'
                  },
                  xl: {
                    root: 'size-10 text-xl'
                  },
                  '2xl': {
                    root: 'size-11 text-[22px]'
                  },
                  '3xl': {
                    root: 'size-12 text-2xl'
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

[AlertA callout to draw user's attention.](/components/alert)[AvatarGroupStack
multiple avatars in a group.](/components/avatar-group)

