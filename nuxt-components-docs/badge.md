<!-- source: https://ui.nuxt.com/components/badge --> # Badge

[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Badge.vue)

A short text to represent a status or a category.

## Usage

### Label

Use the default slot to set the label of the Badge.

    
    
    <template>
      <UBadge>Badge</UBadge>
    </template>
    

You can achieve the same result by using the `label` prop.

label

    
    
    <template>
      <UBadge label="Badge" />
    </template>
    

### Color

Use the `color` prop to change the color of the Badge.

color

neutral

    
    
    <template>
      <UBadge color="neutral">Badge</UBadge>
    </template>
    

### Variant

Use the `variant` props to change the variant of the Badge.

color

neutral

variant

outline

    
    
    <template>
      <UBadge color="neutral" variant="outline">Badge</UBadge>
    </template>
    

### Size

Use the `size` prop to change the size of the Badge.

size

xl

    
    
    <template>
      <UBadge size="xl">Badge</UBadge>
    </template>
    

### Icon

Use the `icon` prop to show an [Icon](/components/icon) inside the Badge.

icon

size

md

color

primary

variant

solid

    
    
    <template>
      <UBadge icon="i-lucide-rocket" size="md" color="primary" variant="solid">Badge</UBadge>
    </template>
    

Use the `leading` and `trailing` props to set the icon position or the
`leading-icon` and `trailing-icon` props to set a different icon for each
position.

trailingIcon

size

md

    
    
    <template>
      <UBadge trailing-icon="i-lucide-arrow-right" size="md">Badge</UBadge>
    </template>
    

### Avatar

Use the `avatar` prop to show an [Avatar](/components/avatar) inside the
Badge.

avatar.src

size

md

color

neutral

variant

outline

    
    
    <template>
      <UBadge
        :avatar="{
          src: 'https://github.com/nuxt.png'
        }"
        size="md"
        color="neutral"
        variant="outline"
      >
        Badge
      </UBadge>
    </template>
    

## Examples

### `class` prop

Use the `class` prop to override the base styles of the Badge.

class

    
    
    <template>
      <UBadge class="font-bold rounded-full">Badge</UBadge>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'span'`| `any`The element or component this component should render as.  
`label`| | ` string | number`  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`variant`| `'solid'`| ` "solid" | "outline" | "soft" | "subtle"`  
`size`| `'md'`| ` "md" | "xs" | "sm" | "lg" | "xl"`  
`icon`| | ` string`Display an icon based on the `leading` and `trailing` props.  
`avatar`| | ` AvatarProps`Display an avatar on the left side.Show properties

  * `as?: any`The element or component this component should render as. Defaults to `'span'`.
  * `src?: string`
  * `alt?: string`
  * `icon?: string`
  * `text?: string`
  * `size?: "md" | "3xs" | "2xs" | "xs" | "sm" | "lg" | "xl" | "2xl" | "3xl"`Defaults to `'md'`.
  * `class?: any`
  * `style?: any`
  * `ui?: { root?: ClassNameValue; image?: ClassNameValue; fallback?: ClassNameValue; icon?: ClassNameValue; }`

  
`leading`| | `boolean`When `true`, the icon will be displayed on the left side.  
`leadingIcon`| | ` string`Display an icon on the left side.  
`trailing`| | `boolean`When `true`, the icon will be displayed on the right side.  
`trailingIcon`| | ` string`Display an icon on the right side.  
`ui`| | ` { base?: ClassNameValue; label?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailingIcon?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`leading`| `{}`  
`default`| `{}`  
`trailing`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        badge: {
          slots: {
            base: 'font-medium inline-flex items-center',
            label: 'truncate',
            leadingIcon: 'shrink-0',
            leadingAvatar: 'shrink-0',
            leadingAvatarSize: '',
            trailingIcon: 'shrink-0'
          },
          variants: {
            buttonGroup: {
              horizontal: 'not-only:first:rounded-e-none not-only:last:rounded-s-none not-last:not-first:rounded-none',
              vertical: 'not-only:first:rounded-b-none not-only:last:rounded-t-none not-last:not-first:rounded-none'
            },
            color: {
              primary: '',
              secondary: '',
              success: '',
              info: '',
              warning: '',
              error: '',
              neutral: ''
            },
            variant: {
              solid: '',
              outline: '',
              soft: '',
              subtle: ''
            },
            size: {
              xs: {
                base: 'text-[8px]/3 px-1 py-0.5 gap-1 rounded-sm',
                leadingIcon: 'size-3',
                leadingAvatarSize: '3xs',
                trailingIcon: 'size-3'
              },
              sm: {
                base: 'text-[10px]/3 px-1.5 py-1 gap-1 rounded-sm',
                leadingIcon: 'size-3',
                leadingAvatarSize: '3xs',
                trailingIcon: 'size-3'
              },
              md: {
                base: 'text-xs px-2 py-1 gap-1 rounded-md',
                leadingIcon: 'size-4',
                leadingAvatarSize: '3xs',
                trailingIcon: 'size-4'
              },
              lg: {
                base: 'text-sm px-2 py-1 gap-1.5 rounded-md',
                leadingIcon: 'size-5',
                leadingAvatarSize: '2xs',
                trailingIcon: 'size-5'
              },
              xl: {
                base: 'text-base px-2.5 py-1 gap-1.5 rounded-md',
                leadingIcon: 'size-6',
                leadingAvatarSize: '2xs',
                trailingIcon: 'size-6'
              }
            }
          },
          compoundVariants: [
            {
              color: 'primary',
              variant: 'solid',
              class: 'bg-primary text-inverted'
            },
            {
              color: 'primary',
              variant: 'outline',
              class: 'text-primary ring ring-inset ring-primary/50'
            },
            {
              color: 'primary',
              variant: 'soft',
              class: 'bg-primary/10 text-primary'
            },
            {
              color: 'primary',
              variant: 'subtle',
              class: 'bg-primary/10 text-primary ring ring-inset ring-primary/25'
            },
            {
              color: 'neutral',
              variant: 'solid',
              class: 'text-inverted bg-inverted'
            },
            {
              color: 'neutral',
              variant: 'outline',
              class: 'ring ring-inset ring-accented text-default bg-default'
            },
            {
              color: 'neutral',
              variant: 'soft',
              class: 'text-default bg-elevated'
            },
            {
              color: 'neutral',
              variant: 'subtle',
              class: 'ring ring-inset ring-accented text-default bg-elevated'
            }
          ],
          defaultVariants: {
            color: 'primary',
            variant: 'solid',
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
            badge: {
              slots: {
                base: 'font-medium inline-flex items-center',
                label: 'truncate',
                leadingIcon: 'shrink-0',
                leadingAvatar: 'shrink-0',
                leadingAvatarSize: '',
                trailingIcon: 'shrink-0'
              },
              variants: {
                buttonGroup: {
                  horizontal: 'not-only:first:rounded-e-none not-only:last:rounded-s-none not-last:not-first:rounded-none',
                  vertical: 'not-only:first:rounded-b-none not-only:last:rounded-t-none not-last:not-first:rounded-none'
                },
                color: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                },
                variant: {
                  solid: '',
                  outline: '',
                  soft: '',
                  subtle: ''
                },
                size: {
                  xs: {
                    base: 'text-[8px]/3 px-1 py-0.5 gap-1 rounded-sm',
                    leadingIcon: 'size-3',
                    leadingAvatarSize: '3xs',
                    trailingIcon: 'size-3'
                  },
                  sm: {
                    base: 'text-[10px]/3 px-1.5 py-1 gap-1 rounded-sm',
                    leadingIcon: 'size-3',
                    leadingAvatarSize: '3xs',
                    trailingIcon: 'size-3'
                  },
                  md: {
                    base: 'text-xs px-2 py-1 gap-1 rounded-md',
                    leadingIcon: 'size-4',
                    leadingAvatarSize: '3xs',
                    trailingIcon: 'size-4'
                  },
                  lg: {
                    base: 'text-sm px-2 py-1 gap-1.5 rounded-md',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs',
                    trailingIcon: 'size-5'
                  },
                  xl: {
                    base: 'text-base px-2.5 py-1 gap-1.5 rounded-md',
                    leadingIcon: 'size-6',
                    leadingAvatarSize: '2xs',
                    trailingIcon: 'size-6'
                  }
                }
              },
              compoundVariants: [
                {
                  color: 'primary',
                  variant: 'solid',
                  class: 'bg-primary text-inverted'
                },
                {
                  color: 'primary',
                  variant: 'outline',
                  class: 'text-primary ring ring-inset ring-primary/50'
                },
                {
                  color: 'primary',
                  variant: 'soft',
                  class: 'bg-primary/10 text-primary'
                },
                {
                  color: 'primary',
                  variant: 'subtle',
                  class: 'bg-primary/10 text-primary ring ring-inset ring-primary/25'
                },
                {
                  color: 'neutral',
                  variant: 'solid',
                  class: 'text-inverted bg-inverted'
                },
                {
                  color: 'neutral',
                  variant: 'outline',
                  class: 'ring ring-inset ring-accented text-default bg-default'
                },
                {
                  color: 'neutral',
                  variant: 'soft',
                  class: 'text-default bg-elevated'
                },
                {
                  color: 'neutral',
                  variant: 'subtle',
                  class: 'ring ring-inset ring-accented text-default bg-elevated'
                }
              ],
              defaultVariants: {
                color: 'primary',
                variant: 'solid',
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
            badge: {
              slots: {
                base: 'font-medium inline-flex items-center',
                label: 'truncate',
                leadingIcon: 'shrink-0',
                leadingAvatar: 'shrink-0',
                leadingAvatarSize: '',
                trailingIcon: 'shrink-0'
              },
              variants: {
                buttonGroup: {
                  horizontal: 'not-only:first:rounded-e-none not-only:last:rounded-s-none not-last:not-first:rounded-none',
                  vertical: 'not-only:first:rounded-b-none not-only:last:rounded-t-none not-last:not-first:rounded-none'
                },
                color: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                },
                variant: {
                  solid: '',
                  outline: '',
                  soft: '',
                  subtle: ''
                },
                size: {
                  xs: {
                    base: 'text-[8px]/3 px-1 py-0.5 gap-1 rounded-sm',
                    leadingIcon: 'size-3',
                    leadingAvatarSize: '3xs',
                    trailingIcon: 'size-3'
                  },
                  sm: {
                    base: 'text-[10px]/3 px-1.5 py-1 gap-1 rounded-sm',
                    leadingIcon: 'size-3',
                    leadingAvatarSize: '3xs',
                    trailingIcon: 'size-3'
                  },
                  md: {
                    base: 'text-xs px-2 py-1 gap-1 rounded-md',
                    leadingIcon: 'size-4',
                    leadingAvatarSize: '3xs',
                    trailingIcon: 'size-4'
                  },
                  lg: {
                    base: 'text-sm px-2 py-1 gap-1.5 rounded-md',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs',
                    trailingIcon: 'size-5'
                  },
                  xl: {
                    base: 'text-base px-2.5 py-1 gap-1.5 rounded-md',
                    leadingIcon: 'size-6',
                    leadingAvatarSize: '2xs',
                    trailingIcon: 'size-6'
                  }
                }
              },
              compoundVariants: [
                {
                  color: 'primary',
                  variant: 'solid',
                  class: 'bg-primary text-inverted'
                },
                {
                  color: 'primary',
                  variant: 'outline',
                  class: 'text-primary ring ring-inset ring-primary/50'
                },
                {
                  color: 'primary',
                  variant: 'soft',
                  class: 'bg-primary/10 text-primary'
                },
                {
                  color: 'primary',
                  variant: 'subtle',
                  class: 'bg-primary/10 text-primary ring ring-inset ring-primary/25'
                },
                {
                  color: 'neutral',
                  variant: 'solid',
                  class: 'text-inverted bg-inverted'
                },
                {
                  color: 'neutral',
                  variant: 'outline',
                  class: 'ring ring-inset ring-accented text-default bg-default'
                },
                {
                  color: 'neutral',
                  variant: 'soft',
                  class: 'text-default bg-elevated'
                },
                {
                  color: 'neutral',
                  variant: 'subtle',
                  class: 'ring ring-inset ring-accented text-default bg-elevated'
                }
              ],
              defaultVariants: {
                color: 'primary',
                variant: 'solid',
                size: 'md'
              }
            }
          }
        })
      ]
    })
    

Expand code

[](https://github.com/nuxt/ui/blob/v3/src/theme/badge.ts "Compound
variants")Some colors in `compoundVariants` are omitted for readability. Check
out the source code on GitHub.

[AvatarGroupStack multiple avatars in a group.](/components/avatar-
group)[BreadcrumbA hierarchy of links to navigate through a
website.](/components/breadcrumb)

